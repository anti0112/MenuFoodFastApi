from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .dish import Dish
from .menu import Menu
from .submenu import Submenu
