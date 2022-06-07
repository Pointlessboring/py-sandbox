locations = {}

active = True

while active:

    name = input("What is your name? (enter 'quit' to exit) ")
    if name == 'quit':
        active = False
        break
    loc  = input("What is your dream vacation spot: ")
    locations[name] = loc

print (locations)

for name, loc in locations.items(): 
    print(f"{name.title()} would like to visit {loc.title()}.")