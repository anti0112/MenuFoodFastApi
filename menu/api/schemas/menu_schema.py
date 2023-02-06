from pydantic import BaseModel


class OrmModeOn(BaseModel):
    class Config:
        orm_mode = True


class BaseMenu(OrmModeOn):
    id: str
    title: str
    description: str


class MenuOut(BaseMenu):
    submenus_count: int
    dishes_count: int


class MenuIn(BaseModel):
    title: str
    description: str

    class Config:
        schema_extra = {
            "example": {"title": "My title", "description": "My description"}
        }
