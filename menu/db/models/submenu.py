from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from menu.db.models import Base


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    menu_id = Column(Integer, ForeignKey("menus.id", ondelete="CASCADE"))
    dishes = relationship("Dish", backref="submenu",
                          lazy="selectin", cascade="all, delete")
