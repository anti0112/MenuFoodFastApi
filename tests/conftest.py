import pytest_asyncio
from httpx import AsyncClient
from menu.core.config import SQLALCHEMY_DATABASE_TEST_URL, REDIS_TEST_URL
from main import get_app


@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    app = await get_app(db_url=SQLALCHEMY_DATABASE_TEST_URL,
                        redis_url=REDIS_TEST_URL,
                        create_url=SQLALCHEMY_DATABASE_TEST_URL)
    async with AsyncClient(app=app, base_url='https://test') as client:
        yield client
