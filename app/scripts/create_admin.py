from sqlmodel import Session

from app.core.database import engine
from app.core.security import hash_password
from app.models.user import User


with Session(engine) as session:
    admin = User(
        username="admin",
        phone="9999999999",
        password_hash=hash_password(
            "admin123"
        ),
        role="ADMIN"
    )

    session.add(admin)
    session.commit()

print("Admin created")