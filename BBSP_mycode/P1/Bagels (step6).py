# Step1 : Generate the random number
# Step2 : Print messages to user & get input
# Step3 : Validate user input against answer
# Step4 : Add loss message. Validate user input better.
# Step5 : Play again query?
# Step6 : Debugging 
            # - sort answer instead of shuffle

import random

MAX_GUESSES = 10
MAX_DIGITS = 3

def main():

    print(f'''Bagels, a deductive logic game.
	By Al Sweigart al@inventwithpython.com
	
	I am thinking of a {format(MAX_DIGITS)}-digit number with no repeated digits.
 	Try to guess what it is. Here are some clues:
	When I say:    That means:
	  Pico         One digit is correct but in the wrong position.
	  Fermi        One digit is correct and in the right position.
	  Bagels       No digit is correct.

	For example, if the secret number was 248 and your guess was 843, the
 	clues would be Fermi Pico.''')

    while True:
        goal = get_secret_number(MAX_DIGITS)
        won = False
        guess_no = 1

        print(f'I have selected a number. you have {MAX_GUESSES} to find it.')
        while guess_no < MAX_GUESSES:
            print(f"\nGuess #{guess_no}")
            guess = input(">")

            if len(guess) == MAX_DIGITS and guess.isdecimal():
                result = check_answer(guess, goal)
                print(result)
                if result == "Fermi Fermi Fermi":
                    print(f"You won in {guess_no} tries.\n")
                    won = True
                    break
                else: 
                    guess_no += 1
            else: 
                print(f"Invalid input! Enter {MAX_DIGITS} digits only")
        if not won:
            print(f"You did not find the secret. It was {goal}\n")
        again = input("Do you want to play again? (enter 'no' to stop)")
        if again == 'no':
            break

def get_secret_number(length):
    base = [str(x) for x in range(0,10)]
    return ''.join(random.sample(base, length))

def check_answer(guess, goal):
    result = []
    for pos in range(len(guess)): 
        if guess[pos] == goal[pos]:
            result.append('Fermi')
        elif guess[pos] in goal:
            result.append('Pico')
    result.sort()
    if result == []:
        return 'Bagels'
    else: 
        return ' '.join(result)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
	main()