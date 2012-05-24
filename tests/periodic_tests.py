import periodic as table

# Testing type_ function
#========================================================================

def testtype_():
    assert table.type_(1) == int
    assert table.type_(15.999) == float
    assert table.type_('hydrogen') == str
    assert table.type_('H') == str

# Testing database queries
#========================================================================
def test_element():
    hydrogen = table.session.query(table.Element).filter_by(name='Hydrogen').first()
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

def test_all():
    testtype_()
    test_element()

if __name__ == '__main__':
    test_all()
