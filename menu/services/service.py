from dataclasses import dataclass

from aioredis import Redis
from fastapi import Depends

from menu.db.redis_cache import redis_stub
from menu.dao.redis_dao import RedisDAO
from menu.dao.dao import Dao
from menu.db.database import dao_stub
from menu.services.dish_services import DishesService
from menu.services.menu_services import MenuService
from menu.services.submenu_services import SubmenuService


def service_stub():
    """Connection for Depends from main.py"""
    raise NotImplementedError


@dataclass
class Services:
    menu_service: MenuService
    submenu_service: SubmenuService
    dishes_service: DishesService


def get_service(dao: Dao = Depends(dao_stub), redis: Redis = Depends(redis_stub)):
    redis = RedisDAO(redis)

    service = Services(
        menu_service=MenuService(dao=dao.menu, main_dao=dao, redis=redis),
        submenu_service=SubmenuService(
            dao=dao.submenu, main_dao=dao, redis=redis),
        dishes_service=DishesService(
            dao=dao.dish, main_dao=dao, redis=redis),
    )

    yield service
