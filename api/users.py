
from typing import Optional,List

import fastapi 
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic_schemas.users import User, UserCreate
from database.db_setup import get_db
from api.utils.users import get_user, get_user_by_email, create_user, get_users


router = fastapi.APIRouter()

@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    users = await get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_created_user = await get_user_by_email(db = db, email = user.email)
    if db_created_user:
       raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await create_user(db, user = user)
    return new_user

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
   db_user  = await get_user(db= db, user_id = user_id)
   if db_user is None:
       raise HTTPException(status_code=404, detail="User not found")
   return db_user