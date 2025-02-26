from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args={},future = True)

SessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()



#DB Utility function
async def get_db():
    async with SessionLocal() as session:
        yield session
        await session.commit()