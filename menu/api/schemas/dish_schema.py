from .menu_schema import BaseMenu, MenuIn


class DishOut(BaseMenu):
    price: str


class DishIn(MenuIn):
    price: float

    class Config:
        schema_extra = {
            "example": {
                "title": "My title",
                "description": "My description",
                "price": 10.00
            }
        }
