from fastapi import (
    APIRouter,
    Depends,
    status
)

from sqlmodel import Session, select

from app.core.database import get_session

from app.dependencies.auth import (
    get_current_user,
    get_current_admin
)

from app.models.user import User
from app.models.plan import Plan

from app.schemas.plan import PlanCreate

from app.services.plan_service import (
    create_plan as create_plan_service
)


router = APIRouter(
    prefix="/plans",
    tags=["Plans"]
)


@router.get("")
def get_plans(
    session: Session = Depends(get_session),
    current_user: User = Depends(
        get_current_user
    )
):
    """
    Get all available plans.
    Requires authenticated user.
    """

    plans = session.exec(
        select(Plan)
    ).all()

    return plans


@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
def create_plan(
    data: PlanCreate,
    session: Session = Depends(get_session),
    current_admin: User = Depends(
        get_current_admin
    )
):
    """
    Create a new plan.
    Admin only.
    """

    plan = create_plan_service(
        session=session,
        plan_data=data.model_dump()
    )

    return plan