from json import loads

from day1 import find_floor, find_basement_entry_char
from day2 import (
    compute_paper_need,
    total_paper_needed,
    compute_ribbon_need,
    total_ribbon_needed
)
from day3 import (
    number_of_distributed_presents,
    number_of_distributed_presents_with_robot
)
from day4 import brute_force_hash_finding


answers = loads(open('answers.json').read())


def test_day_1():
    input_day_1 = open('inputs/day1', 'r').read()
    assert find_floor('(())') == 0
    assert find_floor('()()') == 0
    assert find_floor('(((') == 3
    assert find_floor('(()(()(') == 3
    assert find_floor('))(((((') == 3
    assert find_floor('())') == -1
    assert find_floor('))(') == -1
    assert find_floor(')))') == -3
    assert find_floor(')())())') == -3
    assert find_floor(input_day_1) == answers['day1']['part1']

    assert find_basement_entry_char(')') == 1
    assert find_basement_entry_char('()())') == 5
    assert find_basement_entry_char(input_day_1) == answers['day1']['part2']


def test_day_2():
    f = open('./inputs/day2', 'r').read()
    input_day_2 = f.split('\n')
    assert compute_paper_need(2, 3, 4) == 58
    assert compute_paper_need(1, 1, 10) == 43
    assert total_paper_needed(input_day_2) == answers['day2']['part1']

    assert compute_ribbon_need(2, 3, 4) == 34
    assert compute_ribbon_need(1, 1, 10) == 14
    assert total_ribbon_needed(input_day_2) == answers['day2']['part2']


def test_day_3():
    input_day_3 = open('inputs/day3', 'r').read()
    assert number_of_distributed_presents('>') == 2
    assert number_of_distributed_presents('^>v<') == 4
    assert number_of_distributed_presents('^v^v^v^v^v') == 2

    assert number_of_distributed_presents(input_day_3) == \
        answers['day3']['part1']

    assert number_of_distributed_presents_with_robot('^>') == 3
    assert number_of_distributed_presents_with_robot('^>v<') == 3
    assert number_of_distributed_presents_with_robot('^v^v^v^v^v') == 11

    assert number_of_distributed_presents_with_robot(input_day_3) == \
        answers['day3']['part2']


def test_day_4():
    input_day_4 = open('inputs/day4', 'r').read()
    assert brute_force_hash_finding('abcdef') == 609043
    assert brute_force_hash_finding('pqrstuv') == 1048970

    assert brute_force_hash_finding(input_day_4, 5) == answers['day4']['part1']
    assert brute_force_hash_finding(input_day_4, 6) == answers['day4']['part2']
