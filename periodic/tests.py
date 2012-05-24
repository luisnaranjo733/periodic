import table

# Testing _type function
#========================================================================

assert table._type(1) == int
assert table._type(15.999) == float
assert table._type('hydrogen') == str
assert table._type('H') == str

# Testing database queries
#========================================================================
hydrogen = table.session.query(table._Element).filter_by(name='Hydrogen').first()
tests = [
    1,
    1.00794,
    'H',
    'h',
    'Hydrogen',
    'hydrogen',
]

for test in tests:
    assert hydrogen == table.element(test)
