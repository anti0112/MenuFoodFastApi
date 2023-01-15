from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from core.db import Base


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    submenu_id = Column(Integer, ForeignKey('submenus.id'))
    submenu = relationship("Submenu", back_populates="dishes")
    price = Column(Float(precision=2))


class Submenu(Base):
    __tablename__ = 'submenus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    menu_id = Column(Integer, ForeignKey('menus.id'))
    menu = relationship('Menu', back_populates="submenus")
    dishes = relationship('Dish', back_populates="submenu",
                          cascade="all, delete-orphan")

    @property
    def count_dishes(self):
        return len(self.dishes)


class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    submenus = relationship('Submenu', back_populates="menu",
                            cascade="all, delete-orphan")

    @property
    def count_submenus(self):
        return len(self.submenus)

    @property
    def count_dishes(self):
        return sum([submenu.num_dishes for submenu in self.submenus])
