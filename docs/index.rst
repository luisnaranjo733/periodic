Periodic
====================================

.. toctree::
   :maxdepth: 2

**Periodic** is an `open source`_ simple python API for the periodic table, created by Luis Naranjo

>>> import periodic
>>> element = periodic.element(12)
>>> attributes = ['atomic', 'symbol', 'name', 'mass']
>>> for attribute in attributes:
...     print getattr(element, attribute)
... 
12
Mg
Magnesium
24.305

Installation
============

If you haven't installed pip yet, `here`_ is an excellent guide on how to do so (in the 'Properly Install Python' section).

After you have the that all set up, you can run the following command:

.. _here: http://docs.python-guide.org/en/latest/index.html

>>> pip install periodic

or if you are on a Linux or Mac OS,

>>> sudo pip install periodic

Usage
=====

Retrieve element as an object
-----------------------------

>>> from periodic.table import element
>>> hydrogen = element('hydrogen')
>>> hydrogen.mass
1.0079
>>> hydrogen.symbol
'H'

**Class arguments**

The input for elements can be any of the following, and is case *insensitive*.

* element name (example: hydrogen) - **STRING**
* element symbol (example: H) - **STRING**
* atomic number (example: 1) - **INTEGER**
* atomic mass  (example: 1.0079) - **FLOATING POINT**

**Object attributes**

* symbol
* name
* mass
* atomic
* charge
* type

Periodic mass variables
----------------------- 

Periodic also includes 'loose' atomic mass variables, for quick calculations.

>>> from periodic.mass import *
>>> H
1.0079
>>> H+Cl
36.4609



Interactive shell
-----------------

TO BE IMPLEMENTED

Periodic Table
--------------

There is also a *nice* ascii periodic table available:

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

.. _open source: https://launchpad.net/periodic

.. automodule:: periodic.table
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

