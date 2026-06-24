from sqlmodel import Session, select

from app.core.database import engine, create_db_and_tables
from app.core.config import settings
from app.core.security import hash_password

from app.models.user import User
from app.models.enums import UserRole

def create_admin() -> None:
    # Ensure tables exist before creating admin
    create_db_and_tables()

    with Session(engine) as session:
        existing_admin = session.exec(
            select(User).where(
                User.username == settings.ADMIN_USERNAME
            )
        ).first()

        if existing_admin:
            print("Admin already exists")
            return

        admin = User(
            username=settings.ADMIN_USERNAME,
            phone=settings.ADMIN_PHONE,
            password_hash=hash_password(settings.ADMIN_PASSWORD),
            role=UserRole.ADMIN
        )

        session.add(admin)
        session.commit()

        print("Admin created successfully")

if __name__ == "__main__":
    create_admin()