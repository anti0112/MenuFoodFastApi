from pydantic import BaseModel


class Dishes(BaseModel):
    title: str
    description: str
    price: float


class Submenus(BaseModel):
    title: str
    description: str
    dishes: list[Dishes]


class Menus(BaseModel):
    title: str
    description: str
    submenus: list[Submenus]


class Models(BaseModel):
    __root__: list[Menus]
