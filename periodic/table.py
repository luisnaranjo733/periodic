"""table
====="""
import os

#from sqlalchemy import Column, Integer, String, create_engine, Float
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

__author__ = 'Luis Naranjo'
__email__ = 'luisnaranjo733@hotmail.com'

# Database
#========================================================================
_PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
_INDEX = os.path.join(_PROJECT_ROOT, 'table.db')
_engine = sqlalchemy.create_engine('sqlite:///{path}'.format(path=_INDEX), echo=False)
_Session = sqlalchemy.orm.sessionmaker(bind=_engine)
session = _Session()
_Base = sqlalchemy.ext.declarative.declarative_base()


#========================================================================


class Element(_Base):
    __tablename__ = 'element'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    symbol = sqlalchemy.Column(sqlalchemy.String)  # 'Zr'
    name = sqlalchemy.Column(sqlalchemy.String)  # 'Zirconium
    atomic = sqlalchemy.Column(sqlalchemy.Integer)  # 40
    mass = sqlalchemy.Column(sqlalchemy.Float)  # 91.2240000000

    def __repr__(self):
        return "<Element(symbol='%s', atomic_number='%s')>" % (self.symbol, self.atomic)

#Base.metadata.create_all(_engine)  # init table
_query = session.query(Element)
elements = _query.all()  # List of all of the elements


def _type(_type):
    """Returns a string repr of the 'real _type'."""

    try:
        _type = float(_type)
        if _type.is_integer():
            return int
        if not _type.is_integer():
            return float
    except ValueError:
        return str


def element(_input):
    """Insert docstring here."""

    value = _type(_input)

    if value is int:
        return _query.filter_by(atomic=_input).first()

    if value is float:
        return _query.filter_by(mass=_input).first()

    if value is str:
        _input = _input.capitalize()

    if value is str and 0 < len(_input) <= 2:
        return _query.filter_by(symbol=_input).first()

    if value is str and len(_input) > 2:
        return _query.filter_by(name=_input).first()

table = '''  -----                                                               -----
1 | H |                                                               |He |
  |---+----                                       --------------------+---|
2 |Li |Be |                                       | B | C | N | O | F |Ne |
  |---+---|                                       |---+---+---+---+---+---|
3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
  |---+---+---------------------------------------+---+---+---+---+---+---|
4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
  |---+---+---+------------------------------------------------------------
7 |Fr |Ra |ACT|
  -------------
              -------------------------------------------------------------
   Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
              |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
              -------------------------------------------------------------'''

