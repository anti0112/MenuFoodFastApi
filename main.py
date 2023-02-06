import asyncio

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from menu.api.views import create_xls, dish, menu, stuff_to_db, submenu
from menu.core.config import REDIS_URL, SQLALCHEMY_DATABASE_URL
from menu.db import get_engine
from menu.db.database import DBProvider, dao_stub
from menu.db.models import Base
from menu.db.redis_cache import RedisProvider, redis_stub
from menu.services.service import get_service, service_stub

app = FastAPI()


async def create_models(url):
    engine = get_engine(url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_app(db_url, redis_url, create_url=None):
    global app
    if create_url:
        await create_models(create_url)

    engine = get_engine(db_url)
    pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    provider = DBProvider(pool)
    redis = RedisProvider(redis_url)

    app.dependency_overrides[dao_stub] = provider.get_dao
    app.dependency_overrides[service_stub] = get_service
    app.dependency_overrides[redis_stub] = redis.get_redis

    app.include_router(menu.router, prefix="/api/v1")
    app.include_router(submenu.router, prefix="/api/v1")
    app.include_router(dish.router, prefix="/api/v1")
    app.include_router(create_xls.xlsx_router, prefix="/api/v1")
    app.include_router(stuff_to_db.stuff_router, prefix="/api/v1")

    return app


if __name__ == "__main__":
    asyncio.run(get_app(SQLALCHEMY_DATABASE_URL, REDIS_URL))
    uvicorn.run(app, host="0.0.0.0", port=8000)
