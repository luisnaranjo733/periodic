import csv
import os

from sqlalchemy import Column, Integer, String, create_engine, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Database
#========================================================================
_PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
_INDEX = os.path.join(_PROJECT_ROOT, 'table.db')
engine = create_engine('sqlite:///{path}'.format(path=_INDEX), echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


#========================================================================
__author__ = 'Luis Naranjo'
__email__ = 'luisnaranjo733@hotmail.com'


class Element(Base):
    __tablename__ = 'element'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)  # 'Zr'
    name = Column(String)  # 'Zirconium
    atomic = Column(Integer)  # 40
    mass = Column(Float)  # 91.2240000000

    def __repr__(self):
        return "<Element('%s')>" % self.symbol


#Base.metadata.create_all(engine)  # init table



