from menu.dao.menu_dao import MenuDAO
from menu.schemas.menu_schema import MenuOut, MenuCreate, MenuUpdate
from menu.models import Menu
from fastapi import HTTPException
from typing import List

class MenuService:
    def __init__(self, dao: MenuDAO):
        self.dao = dao

    def get_menu(self, id: int) -> MenuOut:
        menu = self.dao.get(id)
        if menu is None:
            raise HTTPException(status_code=404, detail="menu not found")
        return self.schema_menu_out(menu)

    def get_all_menus(self) -> List[MenuOut]:
        menus = self.dao.get_all()
        return self.schema_menus_out(menus)

    def create_menu(self, menu: MenuCreate) -> MenuOut:
        db_menu = self.dao.create(menu)
        return self.schema_menu_out(db_menu)

    def update_menu(self, id: int, changes: MenuUpdate) -> MenuOut:
        db_menu = self.dao.update(id, changes)
        if db_menu is None:
            raise HTTPException(status_code=404)
        return self.schema_menu_out(db_menu)

    def delete_menu(self, id: int) -> MenuOut:
        menu = self.dao.get(id)
        if menu is None:
            raise HTTPException(status_code=404)
        self.dao.delete(menu)
        return {"status": 'true', "message": "The menu has been deleted"}

    def schema_menu_out(self, menu: Menu) -> MenuOut:
        return MenuOut(
            id=str(menu.id),
            title=menu.title,
            description=menu.description,
            submenus_count=len(menu.submenus),
            dishes_count=sum(len(submenu.dishes) for submenu in menu.submenus)
        )

    def schema_menus_out(self, menus: List[Menu]) -> List[MenuOut]:
        return [MenuOut(
            id=str(menu.id),
            title=menu.title,
            description=menu.description,
            submenus_count=len(menu.submenus),
            dishes_count=sum(len(submenu.dishes) for submenu in menu.submenus))
            for menu in menus]
