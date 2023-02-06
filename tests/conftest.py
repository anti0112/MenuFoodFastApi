import pytest_asyncio
from httpx import AsyncClient

from main import get_app
from menu.core.config import REDIS_TEST_URL, SQLALCHEMY_DATABASE_TEST_URL


@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    app = await get_app(
        db_url=SQLALCHEMY_DATABASE_TEST_URL,
        redis_url=REDIS_TEST_URL,
        create_url=SQLALCHEMY_DATABASE_TEST_URL,
    )
    async with AsyncClient(app=app, base_url="https://test") as client:
        yield client
