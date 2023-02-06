from sqlalchemy.ext.asyncio import AsyncSession

from .all_data_db import TakeDbDAO
from .dish_dao import DishDAO
from .menu_dao import MenuDAO
from .redis_dao import RedisDAO
from .submenu_dao import SubmenuDAO


class Dao:
    menu: MenuDAO
    submenu: SubmenuDAO
    dish: DishDAO
    redis: RedisDAO
    taker: TakeDbDAO

    def __init__(
        self,
        session: AsyncSession,
        menu: type[MenuDAO],
        submenu: type[SubmenuDAO],
        dish: type[DishDAO],
        taker: type[TakeDbDAO],
    ):
        self.menu = menu(session)
        self.submenu = submenu(session)
        self.dish = dish(session)
        self.taker = taker(session)
