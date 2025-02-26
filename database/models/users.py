import enum
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship

from sqlalchemy import Enum as SQLAlchemyEnum
from database.db_setup import Base
from database.models.mixins import Timestamp

class Role(enum.IntEnum):
    admin = 1
    user = 2
    

class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(SQLAlchemyEnum(Role, name="user_role_enum"), default=Role.user)
    username = Column(String(100), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=False)
    password = Column(String(100), nullable=False)


    profile = relationship("Profile", back_populates="owner", uselist=False)
    habits = relationship("Habit", back_populates="user")


class Profile(Timestamp, Base):
    __tablename__ = "profiles"
 
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(Text, nullable=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")
