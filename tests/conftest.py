import asyncio
from typing import Generator
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from menu.core.config import SQLALCHEMY_DATABASE_TEST_URL
from menu.db.models import Base
from main import app

test_engine = create_async_engine(
    SQLALCHEMY_DATABASE_TEST_URL,
)

session = sessionmaker(
    test_engine, class_=AsyncSession, expire_on_commit=False,
)


@pytest.fixture(scope='session')
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url='http://test') as client:
            yield client


@pytest_asyncio.fixture(scope='session')
async def async_session(a_session=session) -> AsyncSession:

    async with a_session() as s:
        async with test_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await test_engine.dispose()
