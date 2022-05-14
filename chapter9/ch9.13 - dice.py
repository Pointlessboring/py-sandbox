from random import randint

class Die():

    def __init__(self, sides):
        self.sides = sides
        self.result = 1

    def roll_die(self):

        self.result = randint(1,self.sides)
        
my_X_die = Die(10)
my_XX_die = Die(20)

for n in range (1,21):
    my_X_die.roll_die()
    my_XX_die.roll_die()
    print(my_X_die.result, my_XX_die.result)
