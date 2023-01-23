from fastapi import APIRouter, Depends
from menu.services.dish_services import DishService
from menu.schemas.dish_schema import DishOut, DishCreate, DishUpdate
from menu.implemented import get_service_dish
from typing import List


router = APIRouter()


@router.post("/menus/{menu_id}/submenus/{submenu_id}/dishes/", response_model=DishOut, status_code=201)
def create_dish(dish: DishCreate, menu_id: int, submenu_id: int,
                dish_service: DishService = Depends(get_service_dish)):
    return dish_service.create_dish(dish, menu_id, submenu_id)


@router.get('/menus/{menu_id}/submenus/{submenu_id}/dishes/', response_model=List[DishOut])
def get_all_dish(submenu_id: int,
                 dish_service: DishService = Depends(get_service_dish)):
    return dish_service.get_all_dishes(submenu_id)


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=DishOut)
def read_dish(dish_id: int, submenu_id: int,
              dish_service: DishService = Depends(get_service_dish)):
    return dish_service.get_dish(dish_id, submenu_id)


@router.patch("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=DishOut)
def update_dish(dish_id: int, submenu_id: int, dish: DishUpdate,
                dish_service: DishService = Depends(get_service_dish)):
    return dish_service.update_dish(dish_id, submenu_id, dish)


@router.delete("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def delete_dish(dish_id: int, submenu_id: int,
                dish_service: DishService = Depends(get_service_dish)):
    return dish_service.delete_dish(dish_id, submenu_id)
