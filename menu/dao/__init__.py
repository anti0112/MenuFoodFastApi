from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemySession:
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session
