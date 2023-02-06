from menu.dao.dao import Dao, DishDAO, MenuDAO, RedisDAO, SubmenuDAO


class ServiceMixin:
    def __init__(self, dao: Dao, redis: RedisDAO):
        self.dao = dao
        self.redis_cache = redis
