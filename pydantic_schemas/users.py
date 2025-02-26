from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    username: str
    password: str
   
class UserCreate(UserBase):
    pass  


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True