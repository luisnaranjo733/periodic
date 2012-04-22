#!/usr/bin/env python

import element_data

#invatomicmass = { 1.0079: 'H'}
#inv_pro = {1:'H'}
#symbols = {'krypton':'Kr'}
#elements = {'Os' : {'mass': 190.2 , 'name' : 'osmium' , 'atomic' : 76 , 'alt' : 'os',  'charge' : (3, 4), 'type': 'metal'} ,
ideas = '''
base class for elements
error class for not found elements
'''

DEBUG = True

def __converter__(element):
    
    try:
        for each in element_data.elements:
            if float(element) == element_data.elements[each]['mass']:
                return float(element)
    except ValueError:    pass
    
    try:
        for each in element_data.elements:
            if int(element) == element_data.elements[each]['atomic']:
                return int(element)
    except ValueError:    pass
    
    try:
        for each in element_data.elements:
            if element == element_data.elements[each]['name']:
                return element
    except ValueError:    pass
    
    try:
        if element.capitalize() in element_data.elements:
            return element.capitalize()
    except KeyError:    pass

def find(element):
    """Takes atomic mass (float only), atomic number (integer or string), symbol, or abbreviation
    of an element.
    Returns the element's capitalized symbol, for use by the `Element class <#elements.Element>`_.

    >>> from chem.elements import *
    >>> find('h')
    'H'
    >>> find(12)
    'Mg'
    >>> find('boron')
    'B'
    >>> find('12')
    'Mg'
    """
    original_input = element
    element = __converter__(element)
    if type(element) == int:
        return element_data.inv_pro[element]
    if type(element) == float:
        return element_data.invatomicmass[element]
    if type(element) == str:
        if len(element) <= 2 and element_data.elements[element]:
            return element
        if len(element) > 2:
            return element_data.symbols[element]
    else:
        print "Error: '%s' not found" % original_input

#elements = {'Os' : {'mass': 190.2 , 'name' : 'osmium' , 'atomic' : 76 , 'alt' : 'os',  'charge' : (3, 4), 'type': 'metal'} ,

class Element(object):
    """Takes a periodic data (ex: 'Ag', '12', 1, 15.999) as input.
    It relies on the `finder function <#elements.find>`_.

    >>> from chem.elements import *
    >>> osmium=Element('Os')
    >>> osmium.name
    'osmium'
    >>> osmium.atomic
    76
    >>> osmium.charge
    (3, 4)
    >>> osmium.type
    'metal'
    """
    
    def __init__(self,symbol):
        self.symbol = find(symbol)
        self.element = element_data.elements[self.symbol]
        self.name = self.element['name']
        self.mass = self.element['mass']
        self.atomic = self.element['atomic']
        self.charge = self.element['charge']
        self.type = self.element['type']


if DEBUG:
    import doctest
    doctest.testmod()

