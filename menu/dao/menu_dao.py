from sqlalchemy import select

from menu.db.models import Menu
from menu.dao import SQLAlchemySession


class MenuDAO(SQLAlchemySession):
    async def _get_menu(self, menu_id: int) -> Menu | None:
        menu = await self.session.get(Menu, menu_id)

        return menu

    async def menu_info(self, menu_id: int) -> Menu | None:
        menu = await self._get_menu(menu_id)

        return menu

    async def get_all_menus(self):
        smtp = select(Menu).order_by(Menu.id)
        Menu_list = (await self.session.scalars(smtp)).all()

        return Menu_list

    async def create_menu(self, title: str, desc: str) -> Menu:
        menu = Menu(title=title, description=desc)

        self.session.add(menu)
        await self.session.commit()
        await self.session.refresh(menu)

        return menu

    async def update_menu(self, menu_id: int, **kwargs):
        menu = await self._get_menu(menu_id)

        for k, v in kwargs.items():
            if hasattr(menu, k):
                setattr(menu, k, v)

        await self.session.commit()
        await self.session.refresh(menu)

        return menu

    async def delete_menu(self, menu_id: int):
        menu = await self._get_menu(menu_id)

        await self.session.delete(menu)
        await self.session.commit()
