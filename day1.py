"""
--- Day 1: Not Quite Lisp ---
Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
"""


def find_floor(input):
    """ Count the number of ( and ) to find the right floor """
    return input.count('(') - input.count(')')


def find_basement_entry_char(input):
    """ Find the position of the ) character that makes the counter equal to -1"""
    counter = 0
    for i, val in enumerate(input):
        counter = counter + 1 if val == '(' else counter - 1
        if counter == -1:
            return i+1
