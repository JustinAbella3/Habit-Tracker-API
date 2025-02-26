from typing import Optional,List

import fastapi 
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic_schemas.habits import Habit, HabitCreate
from database.db_setup import get_db
from api.utils.habits import get_habit, get_habits, update_habit, delete_habit, create_habit

router = fastapi.APIRouter()

@router.get("/habits", response_model=List[Habit])
async def read_habits(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    habits = await get_habits(db, skip=skip, limit=limit)
    return habits

@router.post("/habits", response_model=Habit, status_code=201)
async def create_new_habit(habit: HabitCreate, db: AsyncSession = Depends(get_db)):
    new_habit = await create_habit(db, habit = habit)
    return new_habit

@router.get("/habits/{habit_id}", response_model=Habit)
async def read_habit(habit_id: int, db: AsyncSession = Depends(get_db)):
    db_habit = await get_habit(db= db, habit_id = habit_id)
    if db_habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return db_habit

@router.put("/habits/{habit_id}", response_model=Habit)
async def update_habit_data(habit_id: int, habit: HabitCreate, db: AsyncSession = Depends(get_db)):
    db_habit = await update_habit(db, habit_id = habit_id, habit = habit)
    if db_habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return db_habit