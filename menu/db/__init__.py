import sqlalchemy.orm
from sqlalchemy.ext.asyncio import create_async_engine


def get_engine(url) -> sqlalchemy.ext.asyncio.AsyncEngine:
    """
    Create async engine to database

    :param db: config data
    :return: AsyncEngine
    """
    engine: sqlalchemy.ext.asyncio.AsyncEngine = create_async_engine(
        url, encoding="utf-8", echo=False, future=True
    )

    return engine
