from ..schemas.user import UserRole
from fastapi import Depends, HTTPException, status
from .utils import get_current_user
from ..models.user import User

def require_role(required_role: UserRole):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"user is not authorized"},
                headers=({"WWW-Authenticate": "Bearer"}),
            )
        return current_user
    return role_checker