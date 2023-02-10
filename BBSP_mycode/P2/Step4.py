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


import random
import timeit
from datetime import datetime, timedelta
from collections import Counter

def main():

    MAX_TEST = 100000
    quick = True
    size = 0

    while size == 0 or size > 100:
        size = int(input("What is the group size (max=100)?"))

    print("Processing...\n")
    start = timeit.default_timer()

    # Get Initial group of people
    numbers = get_group(size)
    dups = get_match(numbers)

    # Convert days and duplicates into list of strings
    bdays = get_textdate(numbers)
    ddays = get_textdate(dups)

    # Print the initial birthdays
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

        if quick:
            # The quick version only check for a match. Does not return the matches.
            if test_match(numbers):
                collisions +=1
        else: 
            # The non-quick version check for a matches and return/prints the matches.
            dups = get_match(numbers)
            ddays = ddays = get_match(dups)
            if dups != []:
                print(f"({tests}): Duplicate dates are: {ddays}")
                collisions += 1
        tests += 1

    # Stop timer and calculate runtime.
    stop = timeit.default_timer()
    runtime = stop - start

    # Present final results
    print(f"\nThere was {collisions} collisions in {MAX_TEST} test, or {collisions*100/MAX_TEST}%")
    print(f"Program ran in {runtime} seconds.")

def get_group(size):
    """Returns a list of random numbers that will later be added to Jan 1st to equal a date."""
    return [random.randint(0,364) for x in range (size)]

def get_match(numbers):
    """ Counts number of occurence per item and store dups in variable."""
    counts = Counter(numbers) # Counter returns a dictionary of pairs {Item: Count of item)}
    return [key for key, value in counts.items() if value>1]

def test_match(numbers):
    """ Quick validation on existence of matches without returning the matchs"""
    return numbers != list(dict.fromkeys(numbers))

def get_textdate(numlist):
    """ Converts list of num to list of Str dates"""
    Jan1st = datetime.strptime('01/01/01', "%m/%d/%y")
    return [(Jan1st + timedelta(days=n)).strftime("%b %d") for n in numlist]

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
	main()
    