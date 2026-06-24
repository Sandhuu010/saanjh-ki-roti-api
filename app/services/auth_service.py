from sqlmodel import Session, select

from app.models.user import User


def get_user_by_username(
    username: str,
    session: Session
):
    return session.exec(
        select(User).where(
            User.username == username
        )
    ).first()


def get_user_by_phone(
    phone: str,
    session: Session
):
    return session.exec(
        select(User).where(
            User.phone == phone
        )
    ).first()