from fastapi import Depends , HTTPException, status
from sqlalchemy.orm import Session
from ..database.db import get_db
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from ..models.user import User

load_dotenv()

SECRET_KEY= os.getenv("SECRET_KEY")
ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRY = int(os.getenv("ACCESS_TOKEN_EXPIRY", 30))


pwd_context = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto"
            )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(user_password: str, hashed_password: str):
    return pwd_context.verify(user_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() +timedelta(minutes=ACCESS_TOKEN_EXPIRY)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM )
    return encoded_jwt

def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id = payload.get("user_id")
        if user_id is None:
            raise credential_exception
        user_id = int(user_id)

    except:
        raise credential_exception
    return user_id
    

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"user is not authorized"},
        headers=({"WWW-Authenticate": "Bearer"}),
    )
    user_id = verify_access_token(token, credential_exception)
    user = db.query(User).filter(User.id == user_id).first()
    return user

