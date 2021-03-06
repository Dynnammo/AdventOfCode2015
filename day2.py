"""
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an
order for more. They have a list of the dimensions (length length, width width,
and height height) of each present, and only want to order exactly as much as
they need.

Fortunately, every present is a box (a perfect right rectangular prism), which
makes calculating the required wrapping paper for each gift a little easier:
find the surface area of the box, which is 2*length*width + 2*width*height +
2*height*length. The elves also need a little extra paper for each present:
the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of
wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet
of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of
wrapping paper should they order?

--- Part Two ---
The elves are also running low on ribbon. Ribbon is all the same width, so
they only have to worry about the length they need to order, which they would
again like to be exact.

The ribbon required to wrap a present is the shortest distance around its
sides, or the smallest perimeter of any one face. Each present also requires a
bow made out of ribbon as well; the feet of ribbon required for the perfect bow
is equal to the cubic feet of volume of the present. Don't ask how they tie the
bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap
the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap
the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14
feet.
How many total feet of ribbon should they order?
"""
from importer import open_multiline_line_file


def compute_paper_need(length, width, height):
    sorted_dimensions = sorted([length, height, width])
    required_wrapping_paper = 2*length*width + 2*width*height + 2*height*length
    extra_for_safety = sorted_dimensions[0] * sorted_dimensions[1]
    return required_wrapping_paper + extra_for_safety


def total_paper_needed(input):
    total_paper = 0
    for line in input:
        length, width, height = line.split('x')
        total_paper += compute_paper_need(int(length), int(width), int(height))
    return total_paper


def compute_ribbon_need(length, width, height):
    sorted_dimensions = sorted([length, height, width])
    perimeter = 2 * (sorted_dimensions[0] + sorted_dimensions[1])
    volume = length * width * height
    return perimeter + volume


def total_ribbon_needed(input):
    total_ribbon = 0
    for line in input:
        length, width, height = line.split('x')
        total_ribbon += compute_ribbon_need(
            int(length), int(width), int(height)
        )
    return total_ribbon


# Results
data = open_multiline_line_file('day2')

print("Result for part 1 :", total_paper_needed(data))
print("Result for part 2 :", total_ribbon_needed(data))
