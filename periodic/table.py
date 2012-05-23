import csv
import os

__author__ = 'Luis Naranjo'
__email__ = 'luisnaranjo733@hotmail.com'

_script = os.path.abspath(os.path.dirname(__file__))
_csvfile = open(os.path.join(_script, 'table.csv'))
_reader = csv.reader(_csvfile)

elements = {}

for atomic, mass, name, symbol in _reader:
    value = dict([('atomic', atomic), ('mass', mass), ('name', name)])
    key = symbol
    elements[key] = value

