# Concept: I think I have a more efficient, simpler way to code this project than the book.
# instead of using dates, use number from 1 to 365 in a list and use the set() function to remove duplicates.
# if set(list) != list then there are collisions.
#
# only trick is to create a subfunction to convert a number to a date.
# This is acheive using datetime.timedelta(days=X).

# Step 1: Basic structure, test on timedelta
# Step 2: Set-up Jan1st+365 + data conversion
# Step 3: Test for collisions
# Step 4: Added option for quick match w/o returning the date
# Step 5: Added timer and user options

import random
import timeit
from datetime import datetime, timedelta
from collections import Counter

from matplotlib.pyplot import pause

Jan1st = datetime.strptime('01/01/01', "%m/%d/%y")

def main():

    MAX_TEST = 100000
    qty_test = 0
    size = 0
#    Jan1st = datetime.strptime('01/01/01', "%m/%d/%y")

    while size == 0 or size > 100:
        size = int(input("What is the group size (max=100)? "))

    while qty_test == 0 or qty_test > MAX_TEST:
        qty_test = int(input(f"How many test do you wish to run (max={MAX_TEST})? "))

    quick_answer = ''
    while quick_answer not in ['yes', 'no']:
        quick_answer = input("Use faster matching method ('yes' or 'no')? ")
    quick = (quick_answer == 'yes')
    

    if not quick: 
        details_answer = ''
        while details_answer not in ['yes', 'no']:
            details_answer = input("Provide details for each test ('yes' or 'no')? ")
        details = (details_answer == 'yes')
    else: 
        details = False

    print("Processing...\n")
    start = timeit.default_timer()

    # Get Initial group of people
    numbers = get_group(size)
    dups = get_match(numbers)

    # Print the initial birthdays
    bdays = [(Jan1st+timedelta(days=n)).strftime("%b %d") for n in numbers]
    ddays = [(Jan1st+timedelta(days=n)).strftime("%b %d") for n in dups]
    print(bdays)
    print("\n")
    
    if dups == []:
        print("There are no duplicates in the initial group")
    else: 
        print(f"Duplicate dates are: {ddays}")

    print(f"\nNow running multiple tests, for a total of {qty_test} iterations.")

    tests = 0
    collisions = 0
    
    while tests < qty_test:
        numbers = get_group(size)
        collisions += testing(tests, numbers, quick, details)
        tests += 1

    # Stop timer and calculate runtime.
    stop = timeit.default_timer()
    runtime = stop - start

    # Present final results
    print(f"\nThere was {collisions} collisions in {qty_test} test, or {collisions*100/qty_test}%")
    print(f"Program ran in {runtime} seconds.")

def get_group(size):
    return [random.randint(0,364) for x in range (size)]

def get_match(numbers):
    """ Counts number of occurence per item and store dups in variable."""
    counts = dict(Counter(numbers))
    return [key for key, value in counts.items() if value>1]

def test_match(numbers):
    """ Quick validation on existence of matches without returning the matchs"""
    return numbers != list(dict.fromkeys(numbers))

def testing(tests, numbers, quick, details):
    if quick:
        # The quick version only check for a match. Does not return the matches.
        if test_match(numbers):
            return 1
    else: 
        # The non-quick version check for a matches and return/prints the matches.
        dups = get_match(numbers)

        # Details flag is set. Print the collision dates
        if details: 
            ddays = [(Jan1st+timedelta(days=n)).strftime("%b %d") for n in dups]
            if dups != []:
                print(f"({tests}): Duplicate dates are: {ddays}")
                return 1
    return 0


# If the program is run (instead of imported), run the program:
if __name__ == '__main__':
	main()
    