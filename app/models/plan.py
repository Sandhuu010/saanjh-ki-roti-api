from sqlmodel import SQLModel, Field


class Plan(SQLModel, table=True):
    __tablename__ = "plans"

    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(index=True)

    price_paise: int

    billing_cycle: str

    portion_size: str

    food_cost_per_day_paise: int

    active: bool = True