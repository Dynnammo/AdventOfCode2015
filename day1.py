def findFloor(input):
    """ Count the number of ( and ) to find the right floor """
    return input.count('(') - input.count(')')


def findBasementEntryChar(input):
    """ Find the position of the ) character that makes the counter equal to -1"""
    counter = 0
    for i, val in enumerate(input):
        counter = counter + 1 if val == '(' else counter - 1
        if counter == -1:
            return i+1
