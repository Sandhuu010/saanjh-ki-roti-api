from pydantic import BaseModel


class PlanCreate(BaseModel):
    name: str
    price_paise: int
    billing_cycle: str
    portion_size: str
    food_cost_per_day_paise: int
    active: bool = True