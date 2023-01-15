from fastapi import Depends
from sqlalchemy.orm import Session
from menu.dao.menu_dao import MenuDAO
from menu.services.menu_services import MenuService
from menu.dao.submenu_dao import SubmenuDAO
from menu.services.submenu_services import SubmenuService
from menu.dao.dish_dao import DishDAO
from menu.services.dish_services import DishService
from core.utils import get_db


def get_dao_menu(db: Session = Depends(get_db)):
    return MenuDAO(db=db)


def get_service_menu(dao: MenuDAO = Depends(get_dao_menu)):
    return MenuService(dao)


def get_dao_submenu(db: Session = Depends(get_db)):
    return SubmenuDAO(db=db)


def get_service_submenu(dao: SubmenuDAO = Depends(get_dao_submenu),
                        menu_service: MenuService = Depends(get_service_menu)):
    return SubmenuService(dao=dao, menu_service=menu_service) 


def get_dao_dish(db: Session = Depends(get_db)):
    return DishDAO(db=db)


def get_service_dish(dao: DishDAO = Depends(get_dao_dish),
                     menu_service: MenuService = Depends(get_service_menu),
                     submenu_service: SubmenuService = Depends(get_service_submenu)):
    return DishService(dao=dao, menu_service=menu_service, submenu_service=submenu_service)
