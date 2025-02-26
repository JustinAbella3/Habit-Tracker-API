from sqlalchemy.orm import Session

from database.models.habits import Habit
from pydantic_schemas.habits import HabitCreate

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def get_habit(db: AsyncSession, habit_id: int):
    query = select(Habit).where(Habit.id == habit_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_habits(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(Habit).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def update_habit(db: AsyncSession, habit_id: int, habit: HabitCreate):
    query = select(Habit).where(Habit.id == habit_id)
    result = await db.execute(query)
    db_habit = result.scalar_one_or_none()
    for key, value in habit.dict().items():
        setattr(db_habit, key, value)
    await db.commit()
    await db.refresh(db_habit)
    return db_habit

async def delete_habit(db: AsyncSession, habit_id: int):
    query = select(Habit).where(Habit.id == habit_id)
    result = await db.execute(query)
    db_habit = result.scalar_one_or_none()
    db.delete(db_habit)
    await db.commit()
    return db_habit

#may change when adding user validation.
async def create_habit(db: AsyncSession, habit: HabitCreate):
    db_habit = Habit(name=habit.name, type=habit.type, user_id=habit.user_id, description=habit.description, frequency=habit.frequency)
    db.add(db_habit)
    await db.commit()
    await db.refresh(db_habit)
    return db_habit