import aioredis

def redis_stub():
    raise NotImplementedError


class RedisProvider:
    def __init__(self, url):
        self.pool = aioredis.ConnectionPool.from_url(url)
        self.redis = aioredis.Redis(connection_pool=self.pool, decode_responses=True)

    def get_redis(self) -> aioredis.Redis:
        return self.redis
