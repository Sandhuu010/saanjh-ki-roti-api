from datetime import datetime

from pydantic import BaseModel

from app.models.enums import UserRole


class RegisterRequest(BaseModel):
    username: str
    phone: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    username: str
    phone: str
    role: UserRole
    is_active: bool
    created_at: datetime