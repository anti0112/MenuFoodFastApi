from fastapi import APIRouter, Depends
from menu.services.menu_services import MenuService
from menu.schemas.menu_schema import MenuOut, MenuCreate, MenuUpdate
from menu.implemented import get_service_menu
from typing import List


router = APIRouter()


@router.post("/menus/", response_model=MenuOut, status_code=201)
def create_menu(menu: MenuCreate,
                menu_service: MenuService = Depends(get_service_menu)):
    return menu_service.create_menu(menu)


@router.get("/menus/{menu_id}")
def read_menu(menu_id: int,
              menu_service: MenuService = Depends(get_service_menu)):
    return menu_service.get_menu(menu_id)


@router.get("/menus/", response_model=List[MenuOut])
def read_menus(menu_service: MenuService = Depends(get_service_menu)):
    return menu_service.get_all_menus()


@router.patch("/menus/{menu_id}", response_model=MenuOut)
def update_menu(menu_id: int, menu: MenuUpdate,
                menu_service: MenuService = Depends(get_service_menu)):
    return menu_service.update_menu(menu_id, menu)


@router.delete("/menus/{menu_id}")
def delete_menu(menu_id: int,
                menu_service: MenuService = Depends(get_service_menu)):
    return menu_service.delete_menu(menu_id)
