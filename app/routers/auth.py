from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from fastapi.security import OAuth2PasswordRequestForm

from sqlmodel import Session, select

from app.core.database import get_session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.models.user import User
from app.models.enums import UserRole

from app.schemas.auth import (
    RegisterRequest,
    TokenResponse,
    UserResponse
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    data: RegisterRequest,
    session: Session = Depends(get_session)
):
    existing_user = session.exec(
        select(User).where(
            User.username == data.username
        )
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_BAD_REQUEST,
            detail="Username already exists"
        )

    existing_phone = session.exec(
        select(User).where(
            User.phone == data.phone
        )
    ).first()

    if existing_phone:
        raise HTTPException(
            status_code=status.HTTP_409_BAD_REQUEST,
            detail="Phone number already exists"
        )

    user = User(
        username=data.username,
        phone=data.phone,
        password_hash=hash_password(
            data.password
        ),
        role=UserRole.CUSTOMER
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user


@router.post(
    "/token",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(
            User.username == form_data.username
        )
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(
        form_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_access_token(
        user_id=user.id,
        role=user.role.value
    )

    return TokenResponse(
        access_token=token
    )