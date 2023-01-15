from pydantic import BaseModel
from typing import Optional


class MenuCreate(BaseModel):
    title: str
    description: str


class MenuUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]


class MenuOut(BaseModel):
    id: str
    title: str
    description: str
    submenus_count: int
    dishes_count: int
