from pydantic import BaseModel
from typing import Optional


class DishCreate(BaseModel):
    title: str
    description: str
    price: float


class DishUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]


class DishOut(BaseModel):
    id: str
    title: str
    description: str
    price: str
