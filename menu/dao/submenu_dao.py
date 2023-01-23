from sqlalchemy.orm import Session
from menu.models import Submenu, Menu

from menu.schemas.submenu_schema import (
    SubmenuCreate, SubmenuOut, SubmenuUpdate)
from typing import List

class SubmenuDAO:
    def __init__(self, db: Session):
        self.db = db

    def get(self, submenu_id: int) -> SubmenuOut:
        submenu = self.db.query(Submenu).filter(
            Submenu.id == submenu_id).first()
        if submenu is None:
            return None
        return submenu

    def get_all(self, menu_id: int) -> List[SubmenuOut]:
        submenus = self.db.query(Menu).filter(Menu.id == menu_id).first()
        return submenus

    def create(self, menu_id: int, submenu: SubmenuCreate) -> SubmenuOut:
        db_submenu = Submenu(title=submenu.title,
                             description=submenu.description,
                             menu_id=menu_id)
        self.db.add(db_submenu)
        self.db.commit()
        self.db.refresh(db_submenu)
        return db_submenu

    def update(self, id: int, submenu: SubmenuUpdate) -> SubmenuOut:
        db_submenu = submenu.dict()
        self.db.query(Submenu).filter(Submenu.id == id).update(db_submenu)
        self.db.commit()
        return self.get(id)

    def delete(self, submenu: Submenu):
        self.db.delete(submenu)
        self.db.commit()
