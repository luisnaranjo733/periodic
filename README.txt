Copyright (c) 2012 Jose Luis Naranjo Gomez

chem1.1 CHANGES:
    Accidentally deleted package from cheeseshop - reuploaded and reset versions
    Improved and updated documentation
    Renamed elements.py to search.py - combined all elemental data into a file called elements.py
    
    Implemented a basic math shell for working with elemental masses in search.py.
        Triggered with arithmetic expressions
        Deactivated with 'exit' or 'end' (it's a simple input() statement within a
            while loop.)
        FUTURE IMPLEMENTATION:
            a)Parser that will detect expressions and send them to the math shell
            for processing.
            b)Cleaner code - possible use of objects
    Cleaned up the code a little bit - still needs work (search.py)
    Changed the license from BSD to GNU GPL.
========================================================================
LICENSE http://www.gnu.org/copyleft/gpl.html
========================================================================

Architechture

pychem(module)
     elements.py
     search.py
     game.py
     __init__.py



========================================================================
                elements.py
========================================================================
This is the database that the search.py and game.py use.

Examples:
elements = {'Os' : {'mass': 190.2 , 'name' : 'osmium' , 'atomic' : 76 , 'alt' : 'os',  'charge' : (3, 4), 'type': 'metal'} }

These three are for backwards compatibility with the elements dict.

invatomicmass = { 1.0079: 'H'}
inv_pro = {1:'H'}
symbols = {'krypton':'Kr'}


========================================================================
                search.py
========================================================================
                    
search.py is command-line utility for finding periodic elements, and information about those elements.

USAGE

python search.py object command

    REGULAR EXECUTION

    if __name__ == '__main__' and no additional arguments are given:

        INTERACTIVE MODE is enabled.
        Give it any element's value for any of the commands below.
        
            while in interactive mode:
                if any of these "+ = - / * math addition subtraction division multiplication" are found in the interactive mode:
                    math mode is activated - meaning that if you had written a math problem, then you have to re-write it for the time being
                    sorry!
                    
                    use 'exit' or 'end' to exit
        
    OBJECT

    object can be any atomic number, atomic mass, full name, or abbreviation of any element in the periodic table.
    object can also be the --help flag.


    
    COMMAND

    The command can be any of the following:
        name
        charge
        type
        mass
        atomic
        symbol

    The program will return the command of that given element.
    If no command is given, the program will print out all the information that it has on that element.

    MODULE USAGE

    If search.py is used as a module, then find() function should be used.'

    find() will return the atomic symbol of any elemental command (above) value given.

    This can be used in conjunction with the elements dict described above in the elements.py script.

>>> from chem import search
>>> from elements import elements
>>> search.find(12)
'Mg'
>>> search.find(15.999)
'O'
>>> search.find('h')
'H'
>>> search.find('boron')
'B'
>>> result = search.find('12')
>>> print result
'Mg'
>>>print elements[result]
{'name': 'magnesium', 'charge': 2, 'mass': 24.305, 'atomic': 12, 'alt': 'mg', 'type': 'metal'}
>>>print elements[result]['name']
'magnesium'


========================================================================
                    game.py
========================================================================

game.py is a command line memory game. It is designed to help you learn the periodic elements through testing.

It includes an easy mode, and a hard mode.

Easy mode quizzes the user on random elemental names, and symbols.

Hard mode quizzes the user on random elemental names, symbols, atomic masses, and atomic numbers.

If game.py is executed with python, then the game will automatically start.'

If game is imported, execute it with start()

