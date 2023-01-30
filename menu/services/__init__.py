from menu.dao.dao import RedisDAO, MenuDAO, SubmenuDAO, DishDAO, Dao

class ServiceMixin:
    def __init__(
            self,
            dao: MenuDAO | SubmenuDAO | DishDAO,
            main_dao: Dao | None = None,
            redis: RedisDAO | None = None
    ):
        self.dao = dao
        self.main_dao = main_dao
        self.redis_cache = redis
