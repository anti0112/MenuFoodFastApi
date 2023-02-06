from dataclasses import dataclass

from aioredis import Redis
from fastapi import Depends

from menu.dao.dao import Dao
from menu.dao.redis_dao import RedisDAO
from menu.db.database import dao_stub
from menu.db.redis_cache import redis_stub
from menu.services.db_fill.stuff_db import StuffDbService
from menu.services.dish_services import DishesService
from menu.services.menu_services import MenuService
from menu.services.submenu_services import SubmenuService
from menu.services.task_service import TasksCeleryService
from menu.services.xlsx_generator import XLSXGenerator


def service_stub():
    """Connection for Depends from main.py"""
    raise NotImplementedError


@dataclass
class Services:
    menu_service: MenuService
    submenu_service: SubmenuService
    dishes_service: DishesService
    db_service: StuffDbService
    xlsx_service: XLSXGenerator
    tasks_service: TasksCeleryService


def get_service(
    dao: Dao = Depends(dao_stub), redis: Redis = Depends(redis_stub)
):
    redis = RedisDAO(redis)

    service = Services(
        menu_service=MenuService(dao=dao, redis=redis),
        submenu_service=SubmenuService(dao=dao, redis=redis),
        dishes_service=DishesService(dao=dao, redis=redis),
        db_service=StuffDbService(dao=dao, redis=redis),
        xlsx_service=XLSXGenerator(dao=dao, redis=redis),
        tasks_service=TasksCeleryService(dao=dao, redis=redis),
    )

    yield service
