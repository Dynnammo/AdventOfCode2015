from day1 import (findFloor, findBasementEntryChar)


def test_day_1():
    inputDay1 = open('inputs/day1', 'r').read()
    assert findFloor('(())') == 0
    assert findFloor('()()') == 0
    assert findFloor('(((') == 3
    assert findFloor('(()(()(') == 3
    assert findFloor('))(((((') == 3
    assert findFloor('())') == -1
    assert findFloor('))(') == -1
    assert findFloor(')))') == -3
    assert findFloor(')())())') == -3
    assert findFloor(inputDay1) == 232

    assert findBasementEntryChar(')') == 1
    assert findBasementEntryChar('()())') == 5
    assert findBasementEntryChar(inputDay1) == 1783
