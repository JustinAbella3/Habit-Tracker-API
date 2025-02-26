import enum
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
import datetime

from sqlalchemy import Enum as SQLAlchemyEnum
from database.db_setup import Base
from database.models.mixins import Timestamp

class HabitType(enum.IntEnum):
    good = 1
    bad = 2

class HabitFrequency(enum.IntEnum):
    daily = 1
    weekly = 2
    monthly = 3

class Habit(Timestamp, Base):
    __tablename__ = "habit"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(Text)
    type = Column(Enum(HabitType), nullable = False)
    frequency = Column(Enum(HabitFrequency)) 

    habit_logs = relationship("HabitLog", back_populates="habit")
    user = relationship("User", back_populates="habits")

class HabitLog(Timestamp, Base):
    __tablename__ = "habit_log"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habit.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    is_done = Column(Boolean, nullable=False)
    notes = Column(Text, nullable=True)

    habit = relationship("Habit", back_populates="habit_logs")
