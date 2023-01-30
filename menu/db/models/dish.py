from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, func

from menu.db.models import Base


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Numeric(scale=2), nullable=False)
    submenu_id = Column(Integer, ForeignKey("submenus.id", ondelete="CASCADE"))



