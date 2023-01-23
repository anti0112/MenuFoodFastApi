from sqlalchemy.orm import Session
from menu.models import Dish, Submenu
from menu.schemas.dish_schema import DishCreate, DishOut, DishUpdate
from typing import List

class DishDAO:
    def __init__(self, db: Session):
        self.db = db
       

    def get(self, id: int, submenu_id: int) -> DishOut:
        dish = self.db.query(Dish).filter(Dish.id == id, Dish.submenu_id == submenu_id).first()
        if dish is None:
            return None
        return dish

    def get_all(self, submenu_id: int) -> List[DishOut]:
        submenu = self.db.query(Submenu).filter(Submenu.id == submenu_id).first()
        if submenu is None:
            return None
        dishes = submenu.dishes
        return dishes

    def create(self, dish: DishCreate, submenu_id: int) -> DishOut:
        db_dish = Dish(title=dish.title, price=dish.price, description=dish.description,
                       submenu_id=submenu_id)
        self.db.add(db_dish)
        self.db.commit()
        self.db.refresh(db_dish)
        return db_dish

    def update(self, id: int, submenu_id: int, dish: DishUpdate) -> DishOut:
        db_dish = dish.dict()
        self.db.query(Dish).filter(Dish.id == id, Dish.submenu_id == submenu_id).update(db_dish)
        self.db.commit()
        return self.get(id=id, submenu_id=submenu_id)

    def delete(self, dish: Dish):
        self.db.delete(dish)
        self.db.commit()