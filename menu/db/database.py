import typing
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession
from menu.dao.dao import DishDAO, MenuDAO, Dao, SubmenuDAO


def dao_stub():
    """ Yes, really """
    raise NotImplementedError


class DBProvider:
    def __init__(self, pool):
        self.pool = pool

    async def get_dao(self) -> typing.Generator:
        session: AsyncSession = self.pool()

        try:
            dao = Dao(session, MenuDAO, SubmenuDAO, DishDAO)
            yield dao
        finally:
            await session.close()


def get_db(request: Request):
    return request.state.db
