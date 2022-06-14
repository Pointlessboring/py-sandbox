# Conway's Game of life
#
# Rules: 1) Living cells with 2 or 3 neighbors stay alive
#        2) Dead cells with 3 neighbors become alive
#        3) All other cells are dead in next stage.

# Step 0: Basic Structure and count function.
# Step 1: Display the board


from random import randint
from os import system
import sys

HEIGHT = 40
WIDTH = 80

def main():
    array = [ [randint(0,1) for w in range(WIDTH+1)] for h in range(HEIGHT+1)]

    while True:

        system('clear')
        for line in array:
            print(''.join([str(i) for i in line]))

        


def count_cell(array, x, y):
    count = 0
    for a in range (-1, 2):
        for b in range (-1, 2):
            if a != 0 and b != 0:
                if (a+x) >= 0 and (b+y) >= 0:
                    count += array[y][x]
    return count




# If this program was run (instead of imported), run it:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Conway's game of life, by Pointlessboring")
        sys.exit()  # When Ctrl-C is pressed, end the program.