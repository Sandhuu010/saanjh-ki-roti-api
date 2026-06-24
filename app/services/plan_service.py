from sqlmodel import Session

from app.models.plan import Plan


def create_plan(
    session: Session,
    plan_data: dict
):
    plan = Plan(**plan_data)

    session.add(plan)

    session.commit()

    session.refresh(plan)

    return plan