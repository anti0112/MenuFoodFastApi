from fastapi import HTTPException

from menu.db.models import Submenu
from menu.services import ServiceMixin


class SubmenuService(ServiceMixin):
    async def get_detail(self, submenu_id: int):
        cached_submenu = await self.redis_cache.get_data(f"submenu:{submenu_id}")

        if cached_submenu:
            return cached_submenu
        
        submenu = await self.dao.submenu_info(submenu_id=submenu_id)

        if not submenu:
            raise HTTPException(status_code=404, detail="submenu not found")

        response_data = self.calculate_dishes(submenu)
        await self.redis_cache.save(f"submenu:{submenu_id}", response_data)

        return response_data

    async def get_list(self, menu_id: int):
        cached_submenus = await self.redis_cache.get_data(f"submenus:{menu_id}")

        if cached_submenus:
            return cached_submenus

        menu = await self.main_dao.menu.menu_info(menu_id=menu_id)

        if not menu:
            raise HTTPException(status_code=404, detail="menu not found")

        submenus = self.calculate_submenus(menu.sub_menus)
        await self.redis_cache.save(f"submenus:{menu_id}", submenus)

        return submenus

    async def create(self, menu_id: int, title: str, description: str):
        submenu = await self.dao.create_submenu(menu_id=menu_id, title=title, desc=description)

        await self.redis_cache.clear()

        return self.calculate_dishes(submenu)

    async def update(self, submenu_id: int, **kwargs):
        submenu = await self.dao.submenu_info(submenu_id=submenu_id)

        if not submenu:
            raise HTTPException(status_code=404, detail="menu not found")

        submenu = await self.dao.update_submenu(submenu_id, **kwargs)

        updated_submenu = self.calculate_dishes(submenu)
        await self.redis_cache.save(f"submenu:{submenu.id}", updated_submenu)
        await self.redis_cache.clear(f"submenus:{submenu.menu_id}")

        return updated_submenu

    async def delete(self, submenu_id: int):
        submenu = await self.dao.submenu_info(submenu_id=submenu_id)

        if not submenu:
            raise HTTPException(status_code=404, detail="submenu not found")

        await self.dao.delete_submenu(submenu_id=submenu_id)
        await self.redis_cache.clear()

        return True

    @staticmethod
    def calculate_dishes(submenu: Submenu):
        dishes_count = len(submenu.dishes)

        submenu.dishes_count = dishes_count

        return submenu

    @staticmethod
    def calculate_submenus(submenus: list[Submenu]):
        result_list = list()

        for submenu in submenus:
            dishes_count = len(submenu.dishes)
            submenu.dishes_count = dishes_count

            result_list.append(submenu)

        return result_list
