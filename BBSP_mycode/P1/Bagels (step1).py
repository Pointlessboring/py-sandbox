# Step1 : Generate the random number
# Step2 : Print messages to user

import random

MAX_GUESSES = 10
MAX_DIGITS = 3


def main():

    while True:
        goal = get_secret_number(MAX_DIGITS)
        print(goal)    

def get_secret_number(length):
    base = [x for x in range(0,10)]
    return random.sample(base, length)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
	main()