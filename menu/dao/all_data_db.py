from sqlalchemy import func, select
from sqlalchemy.engine import CursorResult

from menu.dao import SQLAlchemySession
from menu.db.models import Dish, Menu, Submenu


class TakeDbDAO(SQLAlchemySession):
    async def take_all_data(self) -> list:
        dishes = (
            select(
                func.array_agg(
                    func.json_build_object(
                        "title",
                        Dish.title,
                        "description",
                        Dish.description,
                        "price",
                        Dish.price,
                    )
                )
            )
            .scalar_subquery()
            .where(Dish.submenu_id == Submenu.id)
        )

        submenu_dishes = func.array_agg(
            func.json_build_object(
                "title",
                Submenu.title,
                "description",
                Submenu.description,
                "dishes",
                dishes,
            )
        )

        db_data = (
            select(Menu.title, Menu.description, submenu_dishes)
            .join(Menu.sub_menus)
            .group_by(Menu.id)
            .order_by(Menu.id)
        )

        result: CursorResult = await self.session.execute(db_data)
        return result.all()
