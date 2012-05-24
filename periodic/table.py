"""Docstring goes here."""

import csv
import os

from sqlalchemy import Column, Integer, String, create_engine, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'Luis Naranjo'
__email__ = 'luisnaranjo733@hotmail.com'

# Database
#========================================================================
_PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
_INDEX = os.path.join(_PROJECT_ROOT, 'table.db')
engine = create_engine('sqlite:///{path}'.format(path=_INDEX), echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


#========================================================================



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
query = session.query(Element)

def _type(_type):
    """Takes a _type, and returns a string representation of its' real _type."""

    try:
        _type = float(_type)
        if _type.is_integer():
            return int
        if not _type.is_integer():
            return float
    except ValueError:
        return str


def find(_input):
    value = _type(_input)

    if value is int:
        return query.filter_by(atomic=_input).first()

    if value is float:
        return query.filter_by(mass=_input).first()

    if value is str:
        _input = _input.capitalize()

    if value is str and 0 < len(_input) <= 2:
        return query.filter_by(symbol=_input).first()

    if value is str and len(_input) > 2:
        return query.filter_by(name=_input).first()
            

# Testing _type function
#========================================================================

assert _type(1) == int
assert _type(15.999) == float
assert _type('hydrogen') == str



# Testing database queries
#========================================================================
hydrogen = query.filter_by(name='Hydrogen').first()
tests = [
    1,
    1.00794,
    'H',
    'h',
    'Hydrogen',
    'hydrogen',
]

for test in tests:
    assert hydrogen == find(test)
