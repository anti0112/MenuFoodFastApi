from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from menu.db.models import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    sub_menus = relationship(
        "Submenu", backref="menu", lazy="selectin", cascade="all, delete"
    )
