from sqlalchemy import select

from menu.dao import SQLAlchemySession
from menu.db.models import Submenu


class SubmenuDAO(SQLAlchemySession):
    async def _get_submenu(self, submenu_id: int) -> Submenu:
        submenu = await self.session.get(Submenu, submenu_id)

        return submenu

    async def get_all_submenu_for_menu(self, menu_id: int) -> list[Submenu]:
        smtp = (
            select(Submenu)
            .where(Submenu.menu_id == menu_id)
            .order_by(Submenu.id)
        )
        submenu = await self.session.scalars(smtp)

        return submenu.all()

    async def submenu_info(self, submenu_id: int) -> Submenu:
        submenu = await self._get_submenu(submenu_id)

        return submenu

    async def create_submenu(
        self, menu_id: int, title: str, desc: str
    ) -> Submenu:
        submenu = Submenu(menu_id=menu_id, title=title, description=desc)

        self.session.add(submenu)
        await self.session.commit()
        await self.session.refresh(submenu)

        return submenu

    async def update_submenu(self, submenu_id: int, **kwargs):
        submenu = await self._get_submenu(submenu_id)

        for k, v in kwargs.items():
            if hasattr(submenu, k):
                setattr(submenu, k, v)

        await self.session.commit()
        await self.session.refresh(submenu)

        return submenu

    async def delete_submenu(self, submenu_id: int):
        submenu = await self._get_submenu(submenu_id)

        await self.session.delete(submenu)
        await self.session.commit()

        return True
