from fastapi import HTTPException

from menu.services import ServiceMixin


class DishesService(ServiceMixin):
    async def get_detail(self, dish_id: int):
        cached_dish = await self.redis_cache.get_data(f"dish:{dish_id}")

        if cached_dish:
            return cached_dish

        dish = await self.dao.dish.dish_info(dish_id)

        if not dish:
            raise HTTPException(status_code=404, detail="dish not found")

        await self.redis_cache.save(f"dish:{dish_id}", dish)

        return dish

    async def get_list(self):
        cached_dishes = await self.redis_cache.get_data("dishes")

        if cached_dishes:
            return cached_dishes

        dishes = await self.dao.dish.get_all_dishes()
        await self.redis_cache.save("dishes", dishes)

        return dishes

    async def create(
        self, submenu_id: int, title: str, description: str, price: float
    ):
        submenu = await self.dao.submenu.submenu_info(submenu_id=submenu_id)

        if not submenu:
            raise HTTPException(status_code=404, detail="submenu not found")

        dish = await self.dao.dish.create_dish(
            submenu_id=submenu_id, title=title, desc=description, price=price
        )
        await self.redis_cache.clear()

        return dish

    async def update(self, dish_id: int, **kwargs):
        dish = await self.dao.dish.dish_info(dish_id)

        if not dish:
            raise HTTPException(status_code=404, detail="dish not found")

        price = kwargs.get("price")

        if price:
            kwargs["price"] = round(price, 2)

        dish = await self.dao.dish.update_dish(dish_id, **kwargs)

        await self.redis_cache.save(f"dish:{dish.id}", dish)
        await self.redis_cache.clear("dishes")

        return dish

    async def delete(self, dish_id: int):
        dish = await self.dao.dish.dish_info(dish_id=dish_id)

        if not dish:
            raise HTTPException(status_code=404, detail="dish not found")

        await self.dao.dish.delete_dish(dish_id)
        await self.redis_cache.clear()

        return True
