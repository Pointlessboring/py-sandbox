# Concept: I think I have a more efficient, simpler way to code this project than the book.
# instead of using dates, use number from 1 to 365 in a list and use the set() function to remove duplicates.
# if set(list) != list then there are collisions.
#
# only trick is to create a subfunction to convert a number to a date.
# This is acheive using datetime.timedelta(days=X).

# Step 1: Basic structure, test on timedelta
# Step 2: Set-up Jan1st+365 + data conversion
# Step 3: Test for collisions

import random
from datetime import datetime, timedelta
from collections import Counter

def main():

    MAX_TEST = 10
    size = 4

    Jan1st = datetime.strptime('01/01/01', "%m/%d/%y")

    # Get Initial group of people
    numbers = get_group(size)
    dups = get_match(numbers)

    # Print the initial birthdays
    bdays = [(Jan1st+timedelta(days=n)).strftime("%b %d") for n in numbers]
    ddays = [(Jan1st+timedelta(days=n)).strftime("%b %d") for n in dups]
    print("\n",bdays,"\n")
    
    if dups == []:
        print("There are no duplicates in the initial group")
    else: 
        print(f"Duplicate dates are: {ddays}")

    print(f"Testing for {MAX_TEST}")

    tests = 0
    collisions = 0
    while tests < MAX_TEST:
        numbers = get_group(size)
        dups = get_match(numbers)
        ddays = [(Jan1st+timedelta(days=n)).strftime("%b %d") for n in dups]

        if dups != []:
            print(f"({tests}): Duplicate dates are: {ddays}")
            collisions += 1
        tests += 1

    # Present final results
    print(f"\nThere was {collisions} collisions in {MAX_TEST} test, or {collisions*100/MAX_TEST}%")


def get_group(size):
    """Returns a list of random numbers that will later be added to Jan 1st to equal a date."""
    return [random.randint(0,364) for x in range (size)]

def get_match(numbers):
    """ Counts number of occurence per item and store dups in variable."""
    Jan1st = datetime.strptime('01/01/01', "%m/%d/%y")
    counts = Counter(numbers) # Counter returns a dictionary of pairs {Item: Count of item)}
    print(counts)
    print( [(Jan1st+timedelta(days=key)).strftime("%b %d") for key, value in counts.items()])
    return [key for key, value in counts.items() if value > 1]

def test_match(numbers):
    """ Quick validation on existence of matches without returning the matchs"""
    return numbers == set(numbers)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
	main()
    