from menu.services import ServiceMixin
from menu.services.db_fill.db_models import Menus


class XLSXGenerator(ServiceMixin):
    async def get_all_data(self) -> list[dict]:
        data: list = await self.dao.taker.take_all_data()
        menus_list: list[Menus] = self._parse_menu(data)

        menus_dict = [menu.dict() for menu in menus_list]

        return menus_dict

    @staticmethod
    def _parse_menu(menu_data: list) -> list[Menus]:
        menus = list()

        for menu in menu_data:
            title, description, submenus = menu

            parsed_menu = Menus(
                title=title, description=description, submenus=submenus
            )
            menus.append(parsed_menu)

        return menus
