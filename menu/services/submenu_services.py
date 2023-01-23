from menu.dao.submenu_dao import SubmenuDAO
from menu.schemas.submenu_schema import (
    SubmenuOut, SubmenuCreate, SubmenuUpdate)
from menu.models import Submenu
from fastapi import HTTPException
from menu.services.menu_services import MenuService
from typing import List


class SubmenuService:
    def __init__(self, dao: SubmenuDAO, menu_service: MenuService):
        self.dao = dao
        self.menu_service = menu_service

    def get_submenu(self, id: int) -> SubmenuOut:
        submenu = self.dao.get(id)
        if submenu is None:
            raise HTTPException(status_code=404, detail="submenu not found")
        return self.schema_submenu_out(submenu)

    def get_all_submenus(self, menu_id: int) -> List[SubmenuOut]:
        menus = self.dao.get_all(menu_id)
        menus = menus.submenus
        return self.schema_submenus_out(menus)

    def create_submenu(self, submenu: SubmenuCreate, menu_id: int) -> SubmenuOut:
        db_submenu = self.dao.create(submenu, menu_id)
        return self.schema_submenu_out(db_submenu)

    def update_submenu(self, id: int, changes: SubmenuUpdate) -> SubmenuOut:
        db_submenu = self.dao.update(id, changes)
        if db_submenu is None:
            raise HTTPException(status_code=404)
        return self.schema_submenu_out(db_submenu)

    def delete_submenu(self, id: int) -> SubmenuOut:
        submenu = self.dao.get(id)
        if submenu is None:
            raise HTTPException(status_code=404)
        self.dao.delete(submenu)
        return {"status": 'true', "message": "The submenu has been deleted"}

    def schema_submenu_out(self, submenu: Submenu) -> SubmenuOut:
        return SubmenuOut(
            id=str(submenu.id),
            title=submenu.title,
            description=submenu.description,
            dishes_count=len(submenu.dishes))

    def schema_submenus_out(self, submenus: List[Submenu]) -> List[SubmenuOut]:
        return [SubmenuOut(
            id=submenu.id,
            title=submenu.title,
            description=submenu.description,
            dishes_count=len(submenu.dishes)) for submenu in submenus]
