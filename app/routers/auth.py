from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.core.database import get_session
from app.core.security import (
    verify_password,
    create_access_token
)
from app.models.user import User
from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    data: LoginRequest,
    session: Session = Depends(get_session)
):
    statement = select(User).where(
        User.username == data.username
    )

    user = session.exec(statement).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        user_id=user.id,
        role=user.role
    )

    return TokenResponse(
        access_token=token
    )