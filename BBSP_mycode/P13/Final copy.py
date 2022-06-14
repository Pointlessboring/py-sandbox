# Conway's Game of life
#
# Rules: 1) Living cells with 2 or 3 neighbors stay alive
#        2) Dead cells with 3 neighbors become alive
#        3) All other cells are dead in next stage.

# Step 0: Basic Structure and count function.
# Step 1: Display the board
# Step 2: Implement the life 'rules' 
# Step 3: Docstrings, fixes
# Final:  Cleanup, Added option to change the CHR displayed

# Future: 1) One potential improvement would be to increase the array size by 2
#            and exclude the first and last positions. This would remove one check
#         2) an OO version of this is possible. 


from time import sleep
from random import randint
from os import system
from sys import exit

HEIGHT = 20
WIDTH = 50
CHAR_ALIVE = '#'    # Character for living cells
CHAR_DEAD = 'O'     # Character for dead cells
PROB = 10           # Probability of being alive at start

def main():
    """Conway's game of life. my own simple implementation."""

    # Fill an array with random values based on the PROB constant
    array = [ [ (1 if randint(1,100) < PROB else 0) for w in range(WIDTH)] for h in range(HEIGHT)]

    # This is the main loop of the program
    while True:
        system('clear')     # Clear the screen
        print_array(array)  # Print the array

        # Prepare an empty array for the next step.
        new_array = [[0 for w in range(WIDTH)] for h in range(HEIGHT)]

        # Apply the rules of life to the next step of the simulation
        for x in range(WIDTH):
            for y in range(HEIGHT):
                c = count_cell(array, x, y) # Number of neighbors
                v = array[y][x]             # Am I alive?
                
                if v == 0:                  # if dead
                    if c == 3:              # Revive me if 3 neighbors
                        new_array[y][x] = 1
                else:                       # I am alive
                    if c == 2 or c == 3:    # Stay alive if 2 or 3 neighbors
                        new_array[y][x] = 1

        array  = new_array                  # Assign replace original array
        sleep(1)                            # Wait 1 sec.

def count_cell(array, x, y):
    """Calculates the number of living neighbors."""
    # We will loop around the cell adding the values of neighbors

    count = 0
    for a in range (-1, 2): 
        for b in range (-1, 2): 
            if not (a == 0 and b == 0): # this exclude the current cell.

                # Make sure a+x and b+y are within the bounds of the array
                if a+x >= 0 and a+x < WIDTH and b+y >= 0 and b+y < HEIGHT:
                    count += array[b+y][a+x] # if so, add to the count
                   
    return count

def print_array(array):
    """Prints a list of lists (array) of integers, line by line"""
    for line in array:
        print(''.join([ (CHAR_ALIVE if pos ==1 else CHAR_DEAD) for pos in line]))


# If this program was run (instead of imported), run it:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nConway's game of life, by Pointlessboring")
        exit()  # When Ctrl-C is pressed, end the program.