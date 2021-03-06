"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins, you
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of
abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest
such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an
MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
pqrstuv1048970 looks like 000006136ef....

--- Part Two ---

Now find one that starts with six zeroes.
"""
from importer import open_single_line_file
from hashlib import md5


def brute_force_hash_finding(input, lenght_of_0=5):
    hash = md5(input.encode())
    number = -1
    while hash.hexdigest()[:lenght_of_0] != '0' * lenght_of_0:
        number += 1
        entry = input + str(number)
        hash = md5(entry.encode())
    return number


# Results
data = open_single_line_file('day4')

print("Result for part 1 :", brute_force_hash_finding(data, 5))
print("Result for part 1 :", brute_force_hash_finding(data, 6))
