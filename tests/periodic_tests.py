import periodic

# Testing type_ function
#========================================================================


def test_type_():
    assert periodic.type_(1) == int
    assert periodic.type_(15.999) == float
    assert periodic.type_('hydrogen') == str
    assert periodic.type_('H') == str
    return True

# Testing database queries
#========================================================================


def test_correct_elements():
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

    return True


def test_incorrect_elements():
    tests = [
        '125',
        1232,
        'asdfas',
        'HDYROGEN',
    ]
    for test in tests:
        assert periodic.element(test) == None

    return True


def test_asciitable():
    assert periodic.table == '''  -----                                                               -----
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

    return True

tests = [test_type_, test_correct_elements, test_incorrect_elements, test_asciitable]


def test_all():
    passed = 0
    total = len(tests)

    for test in tests:
        result = test()
        if result:
            print("'%s' passed." % test.func_name)
            passed += 1

        if not result:
            print("'%s' failed." % test.func_name)

    print "%d/%d tests passed." % (passed, total)

if __name__ == '__main__':
    test_all()
