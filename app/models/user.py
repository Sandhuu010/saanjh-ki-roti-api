from datetime import datetime
from app.models.enums import UserRole

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)

    username: str = Field(index=True, unique=True)

    phone: str = Field(index=True, unique=True)

    password_hash: str

    role: UserRole = UserRole.CUSTOMER

    is_active: bool = True

    created_at: datetime = Field(default_factory=datetime.utcnow)