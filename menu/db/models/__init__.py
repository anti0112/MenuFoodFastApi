from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()

from .submenu import Submenu
from .dish import Dish
from .menu import Menu
