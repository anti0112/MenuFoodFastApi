from pydantic import BaseModel
from typing import Optional


class SubmenuCreate(BaseModel):
    title: str
    description: str


class SubmenuUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]


class SubmenuOut(BaseModel):
    id: str
    title: str
    description: str
    dishes_count: int
