from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()

from .menu import Menu
from .dish import Dish
from .submenu import Submenu



