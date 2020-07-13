"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
- It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
- It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""

import re


def check_row(string):
    regexp = re.compile(r"(\w)\1")
    return re.search(regexp, string)


def check_vowels(string):
    return len(re.findall("[aeiou]", string)) >= 3


def check_exceptions(string):
    return not bool(re.search("ab|cd|pq|xy", string))


def check_pairs_that_appear_twice(string):
    regexp = re.compile(r"(\w{2})(.*)\1")
    return re.search(regexp, string)


def check_sandwich_letters(string):
    """
    Verify that string contain a sandwich structure, which is two same
    characters with a separator, like xyx
    """
    regexp = re.compile(r"(\w)(\w)\1")
    return re.search(regexp, string)


def is_nice(string, criteria_to_respect):
    for criteria in criteria_to_respect:
        if not criteria(string):
            return False
    return True


def count_nice_string(input, criteria_to_respect):
    counter = 0
    for string in input:
        counter += 1 if is_nice(string, criteria_to_respect) else 0
    return counter


data = open('./inputs/day5', 'r').read().split('\n')

criteria_to_respect_part1 = [check_row, check_vowels, check_exceptions]

criteria_to_respect_part2 = [
    check_pairs_that_appear_twice,
    check_sandwich_letters
]

# Results
print(
    "Result for part 1 :", count_nice_string(data, criteria_to_respect_part1)
)
print(
    "Result for part 2 :", count_nice_string(data, criteria_to_respect_part2)
)
