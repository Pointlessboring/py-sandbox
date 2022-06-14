# Bitmap version of Conway's game of life.
# Inspired from https://www.tutorialspoint.com/conway-s-game-of-life-using-python
# 
# Very interesting/clever use of array functions.

import numpy as np
import matplotlib.pyplot as plt
import argparse, time

HEIGHT = 100
WIDTH = 100

class Board(object):
   """This is the main class. hold the board and code to display"""

   def __init__(self, size):
      """Initialize the Board. Fill it with some cells."""
      self.state = np.random.randint(2, size = size)
      self.engine = Engine(self)
      self.iteration = 0
      
   def animate(self):
      """Sets the display for the board and iterates forever."""
      i = self.iteration
      im = None
      plt.title("Conway's Game of Life")
      while True:
         if i == 0:
            plt.ion()
            im = plt.imshow(self.state, vmin = 0, vmax = 2, cmap = plt.cm.gray)
         else:
            im.set_data(self.state)
         i += 1
         self.engine.applyRules()
         print(f"Life Cycle: {i} Birth: {self.engine.nBirth} Survive: {self.engine.nSurvive}")
         plt.pause(0.01)

class Engine(object):
   def __init__(self, board):
      self.state = board.state

   def countNeighbors(self):
      """Return an array with number of neighbors."""
      state = self.state
      n = (state[0:-2,0:-2] + state[0:-2,1:-1] + state[0:-2,2:] + state[1:-1,0:-2] + 
            state[1:-1,2:] + state[2:,0:-2] + state[2:,1:-1] + state[2:,2:])
      return n

   def applyRules(self):
      """
      Another function making clever use of array functions.

      """

      n = self.countNeighbors()
      state = self.state

      # Birth will equal a boolean array. True if 3 neighbors & cell = 0 
      birth = (n == 3) & (state[1:-1,1:-1] == 0)

      # Survive is a boolean array. True if 2/3 neighbors & cell = 1
      survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1)

      # Wipe State
      state[...] = 0

      # if True in Birth or survive arrays, then put 1 in state
      state[1:-1,1:-1][birth | survive] = 1

      # Calculate the number of non-zero in Birth
      self.nBirth = np.sum(birth)

      # Calculate the number of non-zero in Survive
      self.nSurvive = np.sum(survive)
      return state

def main():
   board = Board((HEIGHT,WIDTH))
   board.animate()

if __name__ == '__main__':
   main()