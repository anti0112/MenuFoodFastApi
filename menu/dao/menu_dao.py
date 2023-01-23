from sqlalchemy.orm import Session
from menu.models import Menu
from menu.schemas.menu_schema import MenuCreate, MenuOut, MenuUpdate
from typing import List

class MenuDAO:
    def __init__(self, db: Session):
        self.db = db

    def get(self, id: int) -> MenuOut:
        menu = self.db.query(Menu).filter(Menu.id == id).first()
        if menu is None:
            return None
        return menu

    def get_all(self) -> List[MenuOut]:
        menus = self.db.query(Menu).all()
        return menus

    def create(self, menu: MenuCreate) -> MenuOut:
        db_menu = Menu(title=menu.title, description=menu.description)
        self.db.add(db_menu)
        self.db.commit()
        self.db.refresh(db_menu)
        return db_menu

    def update(self, id: int, menu: MenuUpdate) -> MenuOut:
        db_menu = menu.dict()
        self.db.query(Menu).filter(Menu.id == id).update(db_menu)
        self.db.commit()
        return self.get(id)

    def delete(self, menu: Menu):
        self.db.delete(menu)
        self.db.commit()
