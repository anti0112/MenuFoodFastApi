from fastapi import APIRouter, Depends
from menu.services.submenu_services import SubmenuService
from menu.schemas.submenu_schema import SubmenuOut, SubmenuCreate, SubmenuUpdate
from menu.implemented import get_service_submenu

router = APIRouter()


@router.post("/menus/{menu_id}/submenus/", response_model=SubmenuOut, status_code=201)
def create_submenu_by_menu(submenu: SubmenuCreate, menu_id: int,
                           submenu_service: SubmenuService = Depends(get_service_submenu)):
    return submenu_service.create_submenu(menu_id, submenu)


@router.get("/menus/{menu_id}/submenus/", response_model=list[SubmenuOut])
def read_submenus_by_menu(menu_id: int,
                          submenu_service: SubmenuService = Depends(get_service_submenu)):
    return submenu_service.get_all_submenus(menu_id)


@router.get("/menus/{menu_id}/submenus/{submenu_id}", response_model=SubmenuOut)
def read_submenu(submenu_id: int,
                 submenu_service: SubmenuService = Depends(get_service_submenu)):
    return submenu_service.get_submenu(submenu_id)


@router.patch("/menus/{menu_id}/submenus/{submenu_id}", response_model=SubmenuOut)
def update_submenu(submenu_id: int, submenu: SubmenuUpdate,
                   submenu_service: SubmenuService = Depends(get_service_submenu)):
    return submenu_service.update_submenu(submenu_id, submenu)


@router.delete("/menus/{menu_id}/submenus/{submenu_id}")
def delete_submenu(submenu_id: int,
                   submenu_service: SubmenuService = Depends(get_service_submenu)):
    return submenu_service.delete_submenu(submenu_id)
