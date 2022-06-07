from random import choice

universe = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', 'g', 'h', 'i', 'j']

my_ticket = ['1', '2', '3', '4']
loop = 0

while True:
    winning = []
    loop += 1
    for n in range (1,5):
        winning.append(choice(universe))
    if winning == my_ticket:
        break

print(f"There were {loop} draws to pull {my_ticket}")