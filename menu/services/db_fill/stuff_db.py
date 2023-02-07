import pydantic

from menu.services import ServiceMixin
from menu.services.db_fill.db_models import Menus, Models


class StuffDbService(ServiceMixin):
    DATA_PATH = "./test_data_menu.json"

    async def create_stuff_db(self):
        menus: list[Menus] = self.read_db_data().__root__

        for menu in menus:
            created_menu = await self.dao.menu.create_menu(
                title=menu.title, desc=menu.description
            )

            for submenu in menu.submenus:
                created_submenu = await self.dao.submenu.create_submenu(
                    menu_id=created_menu.id,
                    title=submenu.title,
                    desc=submenu.description,
                )

                for dish in submenu.dishes:
                    await self.dao.dish.create_dish(
                        submenu_id=created_submenu.id,
                        title=dish.title,
                        desc=dish.description,
                        price=dish.price,
                    )

    def read_db_data(self) -> Models:
        menus = pydantic.parse_file_as(path=self.DATA_PATH, type_=Models)

        return menus
