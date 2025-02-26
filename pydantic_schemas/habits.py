from pydantic import BaseModel, Field
from datetime import datetime

class HabitBase(BaseModel):
   name: str
   type: int
   user_id: int
   description: str = Field(default="")
   frequency: int = Field(default=1)

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True