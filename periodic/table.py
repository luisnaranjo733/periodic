import os as _os
from sys import exit

import sqlalchemy as _sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative

# Database
#========================================================================
_project_root = _os.path.abspath(_os.path.dirname(__file__))
_index = _os.path.join(_project_root, 'table.db')
_engine = _sqlalchemy.create_engine('sqlite:///{path}'.format(path=_index))
_Session = _sqlalchemy.orm.sessionmaker(bind=_engine)
session = _Session()
_Base = _sqlalchemy.ext.declarative.declarative_base()

#========================================================================


class Element(_Base):
    __tablename__ = 'element'
    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True)
    symbol = _sqlalchemy.Column(_sqlalchemy.String)  # 'Zr'
    name = _sqlalchemy.Column(_sqlalchemy.String)  # 'Zirconium
    atomic = _sqlalchemy.Column(_sqlalchemy.Integer)  # 40
    mass = _sqlalchemy.Column(_sqlalchemy.Float)  # 91.2240000000

    def __repr__(self):
        representation = "<Element('%s', '%s')>"
        return representation % (self.symbol, self.atomic)

elements = session.query(Element).order_by(Element.atomic).all()  # Ordered list of all of the elements


def type_(type_):
    """Returns a string repr of the 'real type_'."""

    try:
        type_ = float(type_)
        if type_.is_integer():
            return int
        if not type_.is_integer():
            return float
    except ValueError:
        return str


def element(_input):
    """Takes periodic data as input, and returns the correct element."""

    value = type_(_input)

    if value is int:
        return session.query(Element).filter_by(atomic=_input).first()

    if value is float:
        return session.query(Element).filter_by(mass=_input).first()

    if value is str:
        _input = _input.capitalize()

    if value is str and 0 < len(_input) <= 2:
        return session.query(Element).filter_by(symbol=_input).first()

    if value is str and len(_input) > 2:
        return session.query(Element).filter_by(name=_input).first()

attributes = ['atomic', 'symbol', 'name', 'mass']  # Attributes in an Element instance

#  TODO: Add math support for elements in interative_shell
def interactive_shell():
    usage = """Enter any of the following periodic values of the element you are looking for:
\t{attributes}
""".format(attributes=str(attributes))

    print(usage)
    print("Use ^C or type 'exit' to exit.")

    buff = '=' * 72
    while True:
        try:
            print(buff)
            query = raw_input("> ")
            if query == 'exit':
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            print("\nBye!")
            exit(0)
        element_ = element(query)
        try:
            values = [attribute + ": %s" % getattr(element_, attribute) for attribute in attributes]
        except AttributeError:
            print("'{query}' is not valid!".format(query=query))
            print(usage)
            continue

        for line in values:
            print(line)

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

if __name__ == '__main__':
    interactive_shell()
