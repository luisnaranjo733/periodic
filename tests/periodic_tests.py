import periodic

# Testing type_ function
#========================================================================

def test_type_():
    assert periodic.type_(1) == int
    assert periodic.type_(15.999) == float
    assert periodic.type_('hydrogen') == str
    assert periodic.type_('H') == str

# Testing database queries
#========================================================================
def test_element():
    hydrogen = periodic.session.query(periodic.Element).filter_by(name='Hydrogen').first()
    tests = [
        1,
        '1',
        1.00794,
        '1.00794',
        'H',
        'h',
        'Hydrogen',
        'hydrogen',
    ]

    for test in tests:
        assert hydrogen == periodic.element(test)

def test_all():
    test_type_()
    test_element()

if __name__ == '__main__':
    test_all()
