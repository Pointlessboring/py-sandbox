# Conway's Game of life
#
# Rules: 1) Living cells with 2 or 3 neighbors stay alive
#        2) Dead cells with 3 neighbors become alive
#        3) All other cells are dead in next stage.

# Step 0: Basic Structure and count function.
# Step 1: Display the board
# Step 2: Implement the life 'rules' 

from time import sleep
from random import randint
from os import system
import sys

HEIGHT = 80
WIDTH = 50

def main():
    array = [ [randint(0,1) for w in range(WIDTH)] for h in range(HEIGHT)]
       
    while True:
        system('clear')
        print_array(array)

        new_array = [[0 for w in range(WIDTH)] for h in range(HEIGHT)]

        for x in range(WIDTH):
            for y in range(HEIGHT):
                c = count_cell(array, x, y)
                v = array[y][x]
                new_array[y][x] = 0
                if v == 0:
                    if c == 3:
                        new_array[y][x] = 1
                else:
                    if c == 2 or c == 3:
                        new_array[y][x] = 1
        array  = new_array
        sleep(1)

def count_cell(array, x, y):
    count = 0
    for a in range (-1, 2):
        for b in range (-1, 2):
            if not (a == 0 and b == 0):
                if a+x >= 0 and a+x < WIDTH and b+y >= 0 and b+y < HEIGHT:
                    count += array[b+y][a+x]
    return count

def print_array(array):
        # system('clear')
        for line in array:
            print(''.join([str(i) for i in line]))


# If this program was run (instead of imported), run it:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Conway's game of life, by Pointlessboring")
        sys.exit()  # When Ctrl-C is pressed, end the program.