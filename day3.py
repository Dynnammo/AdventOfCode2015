"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""


def number_of_distributed_presents(input):
    registered_positions = get_positions_from_path(input)
    return len(registered_positions)


def number_of_distributed_presents_with_robot(input):
    santa_input = input[::2]
    robot_input = input[1::2]

    santa_positions = get_positions_from_path(santa_input)
    robot_positions = get_positions_from_path(robot_input)

    santa_positions.update(robot_positions)
    return len(santa_positions)


def get_positions_from_path(instructions):
    current_position = [0, 0]
    registered_positions = set(((0, 0),))
    for char in instructions:
        if char == 'v':
            current_position[0] -= 1
        elif char == '^':
            current_position[0] += 1
        elif char == '>':
            current_position[1] += 1
        elif char == '<':
            current_position[1] -= 1
        registered_positions.add(tuple(current_position))
    return registered_positions


data = open('./inputs/day3', 'r').read()

print(number_of_distributed_presents(data))