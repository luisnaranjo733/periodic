import csv
import os

__author__ = 'Luis Naranjo'
__email__ = 'luisnaranjo733@hotmail.com'

_script = os.path.abspath(os.path.dirname(__file__))
_csvfile = open(os.path.join(_script, 'table.csv'))
_reader = csv.reader(_csvfile)

elements = {}

for atomic, mass, name, symbol in _reader:
    elements[symbol] = dict([
        ('atomic', atomic), 
        ('mass', mass), 
        ('name', name)])

def convert(element):
    """Convert any element-string into its' corresponding symbol, if it is a real element."""

    try:
        element = float(element)
    except ValueError: pass


    if isinstance(element, str): print "string"

class element(object):
    def __init__(self, _input):
        self.input = _input

print elements['H']
