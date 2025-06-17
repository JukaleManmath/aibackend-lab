from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UserBase(BaseModel):
    email: str
    full_name: str

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.user

class UserResponse(UserBase):
    id: int
    role: UserRole
    created_at: datetime
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
    

