from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from menu.dao.dao import Dao, DishDAO, TakeDbDAO, MenuDAO, SubmenuDAO


def dao_stub():
    raise NotImplementedError


class DBProvider:
    def __init__(self, pool):
        self.pool = pool

    async def get_dao(self) -> AsyncGenerator:
        session: AsyncSession = self.pool()

        try:
            dao = Dao(session, MenuDAO, SubmenuDAO, DishDAO, TakeDbDAO)
            yield dao
        finally:
            await session.close()


def get_db(request: Request):
    return request.state.db
