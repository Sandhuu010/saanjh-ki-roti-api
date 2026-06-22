from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.core.database import get_session
from app.models.plan import Plan
from app.schemas.plan import PlanCreate

router = APIRouter(
    prefix="/plans",
    tags=["Plans"]
)


@router.get("")
def get_plans(
    session: Session = Depends(get_session)
):
    plans = session.exec(
        select(Plan)
    ).all()

    return plans


@router.post("")
def create_plan(
    data: PlanCreate,
    session: Session = Depends(get_session)
):
    plan = Plan(
        **data.model_dump()
    )

    session.add(plan)
    session.commit()
    session.refresh(plan)

    return plan