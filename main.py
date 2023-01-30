from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from menu.api.views import menu, dish, submenu

from menu.db import get_engine
from menu.core.config import SQLALCHEMY_DATABASE_URL, REDIS_URL

from menu.db.redis_cache import redis_stub, RedisProvider
from menu.db.database import DBProvider, dao_stub
from menu.services.service import get_service, service_stub


app = FastAPI()

engine = get_engine(SQLALCHEMY_DATABASE_URL)
pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
provider = DBProvider(pool)
redis = RedisProvider(REDIS_URL)

app.dependency_overrides[dao_stub] = provider.get_dao
app.dependency_overrides[service_stub] = get_service
app.dependency_overrides[redis_stub] = redis.get_redis

app.include_router(menu.router, prefix="/api/v1")
app.include_router(submenu.router, prefix="/api/v1")
app.include_router(dish.router, prefix="/api/v1")
