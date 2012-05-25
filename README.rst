Periodic
********

A python API/console script for the periodic table. 

Created by Luis Naranjo <luisnaranjo733@hotmail.com>

Documentation at http://periodic.readthedocs.org

Installation
************

::

pip install periodic

Basic Usage
***********

Retrieve element as an object
=============================

>>> from periodic import element
>>> hydrogen = element('hydrogen')
>>> hydrogen.mass
1.0079

Advanced database queries (using sqlalchemy)
=============================================

>>> from periodic.table import session
>>> session.query(Element).order_by(Element.mass).all()[-4:]
[<Element('Uup', '115')>, <Element('Uuq', '114')>, <Element('Uuh', '116')>, <Element('Uuo', '118')>]

ASCII Table
===========

>>> import periodic
>>> print periodic.table
  -----                                                               -----
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
              -------------------------------------------------------------

Interactive shell (Console script)
==================================

Periodic provides an originally named console script called 'periodic'.

It's usage for now is limited to periodic table reference.

In the future, it will be able to do with elements!
::

    $ periodic
    Enter any of the following periodic values of the element you are looking for:
	    ['atomic', 'symbol', 'name', 'mass']

    Use ^C or type 'exit' to exit.
    ========================================================================
    > 12
    atomic: 12
    symbol: Mg
    name: Magnesium
    mass: 24.305
    ========================================================================
    > uranium
    atomic: 92
    symbol: U
    name: Uranium
    mass: 238.02891
    ========================================================================
    > H
    atomic: 1
    symbol: H
    name: Hydrogen
    mass: 1.00794
    ========================================================================
    > 15.9994
    atomic: 8
    symbol: O
    name: Oxygen
    mass: 15.9994
    ========================================================================

