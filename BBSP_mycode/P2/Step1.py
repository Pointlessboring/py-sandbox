# Concept: I think I have a more efficient, simpler way to code this project than the book.
# instead of using dates, use number from 1 to 365 in a list and use the set() function to remove duplicates.
# if set(list) != list then there are collisions.
#
# only trick is to create a subfunction to convert a number to a date.
# This is acheive using datetime.timedelta(days=X).

# Step 1: Basic structure, test on timedelta

import random
from datetime import datetime, timedelta

def main():

    Jan1st = datetime.strptime('01/01/01', "%m/%d/%y")
    int_list = get_group(10)
    print(Jan1st)
    print(int_list)
    for x in int_list:
        print(Jan1st+timedelta(days=x))

def get_group(number):
    return [random.randint(0,364) for x in range (number)]

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
	main()