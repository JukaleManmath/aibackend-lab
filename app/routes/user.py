from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from ..models.user import User
from ..schemas.user import UserBase, UserResponse, UserCreate
from sqlalchemy.orm import Session
from ..database.db import get_db
from ..auth.utils import hash_password, verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from ..auth.role_checker import require_role

router = APIRouter(prefix="/users", tags=["Users CRUD"])

@router.post("/register", tags=["register a user"], status_code=status.HTTP_201_CREATED, response_model=list[UserResponse])
async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user_password = user_data.password
    hashed_password = hash_password(user_password)
    new_user = User(email= user_data.email,
                    password= hashed_password,
                    full_name = user_data.full_name,
                    role = user_data.role
                    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return [new_user]

@router.post("/login", status_code=status.HTTP_200_OK, tags=["Authentication"])
async def user_login(user_login_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_login_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect email is entered",
                            headers={"WWW-Authenticate": "Bearer"},
                            )
    if not verify_password(user_login_data.password , user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect password is entered",
                            headers={"WWW-Authenticate": "Bearer"},
                            )
    access_token = create_access_token(data={"user_id": user.id})
    return {"access_token": access_token,"token_type": "bearer"}


@router.get("/admin-only", tags=["requesting all users"], status_code=status.HTTP_200_OK, response_model=list[UserResponse])
async def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(require_role("admin"))):
    users = db.query(User).all()
    return users


@router.get("/me", tags=["Protected"])
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user