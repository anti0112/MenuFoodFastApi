from menu.dao.dish_dao import DishDAO
from menu.schemas.dish_schema import DishOut, DishCreate, DishUpdate
from menu.models import Dish
from fastapi import HTTPException
from menu.services.menu_services import MenuService
from menu.services.submenu_services import SubmenuService


class DishService:
    def __init__(self, dao: DishDAO, menu_service: MenuService, submenu_service: SubmenuService):
        self.dao = dao
        self.menu_service = menu_service
        self.submenu_service = submenu_service

    def get_dish(self, id: int, submenu_id: int) -> DishOut:
        dish = self.dao.get(id, submenu_id)
        if dish is None:
            raise HTTPException(status_code=404, detail="dish not found")
        return self.schema_dish_out(dish)

    def get_all_dishes(self, submenu_id: int) -> list[DishOut]:
        dishes = self.dao.get_all(submenu_id)
        if dishes is None:
            return []
        return self.schema_dishes_out(dishes)

    def create_dish(self, dish: DishCreate, menu_id: int, submenu_id: int) -> DishOut:
        menu = self.menu_service.get_menu(menu_id)
        if not menu:
            raise HTTPException(status_code=400, detail="menu not found")
        submenu = self.submenu_service.get_submenu(submenu_id)
        if not submenu:
            raise HTTPException(status_code=400, detail="submenu not found")
        db_dish = self.dao.create(dish, submenu_id)
        return self.schema_dish_out(db_dish)

    def update_dish(self, id: int, submenu_id: int, changes: DishUpdate) -> DishOut:
        db_dish = self.dao.update(id, submenu_id, changes)
        if db_dish is None:
            raise HTTPException(status_code=404)
        return self.schema_dish_out(db_dish)

    def delete_dish(self, id: int, submenu_id: int) -> DishOut:
        dish = self.dao.get(id, submenu_id)
        if dish is None:
            raise HTTPException(status_code=404)
        self.dao.delete(dish)
        return {"status": 'true', "message": "The dish has been deleted"}

    def schema_dish_out(self, dish: Dish) -> DishOut:
        return DishOut(
            id=str(dish.id),
            title=dish.title,
            description=dish.description,
            price=dish.price)

    def schema_dishes_out(self, dishes: list[Dish]) -> list[DishOut]:
        return [DishOut(
            id=str(dish.id),
            title=dish.title,
            description=dish.description,
            price=dish.price) for dish in dishes]
