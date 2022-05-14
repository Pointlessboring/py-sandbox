from random import choice

universe = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', 'g', 'h', 'i', 'j']

winning = []
for n in range (1,5):
    winning.append(choice(universe))

print(winning)