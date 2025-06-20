from app.database.db import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy import Enum as SqlEnum
import enum

class UserRole(str,enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    role = Column(SqlEnum(UserRole), nullable=False, server_default="user")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
