from json import loads

from day1 import (find_floor, find_basement_entry_char)
from day2 import (
    compute_paper_need,
    total_paper_needed,
    compute_ribbon_need,
    total_ribbon_needed
)

answers = loads(open('answers.json').read())


def test_day_1():
    inputDay1 = open('inputs/day1', 'r').read()
    assert find_floor('(())') == 0
    assert find_floor('()()') == 0
    assert find_floor('(((') == 3
    assert find_floor('(()(()(') == 3
    assert find_floor('))(((((') == 3
    assert find_floor('())') == -1
    assert find_floor('))(') == -1
    assert find_floor(')))') == -3
    assert find_floor(')())())') == -3
    assert find_floor(inputDay1) == answers['day1']['part1']

    assert find_basement_entry_char(')') == 1
    assert find_basement_entry_char('()())') == 5
    assert find_basement_entry_char(inputDay1) == answers['day1']['part2']


def test_day_2():
    f = open('./inputs/day2', 'r').read()
    input_day_2 = f.split('\n')
    assert compute_paper_need(2, 3, 4) == 58
    assert compute_paper_need(1, 1, 10) == 43
    assert total_paper_needed(input_day_2) == answers['day2']['part1']

    assert compute_ribbon_need(2, 3, 4) == 34
    assert compute_ribbon_need(1, 1, 10) == 14
    assert total_ribbon_needed(input_day_2) == answers['day2']['part2']
