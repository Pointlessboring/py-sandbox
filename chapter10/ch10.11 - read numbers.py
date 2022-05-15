import json

filename = 'favorite_number.txt'

try:
    with open(filename, 'r') as f:
        numbers = f.read()

except FileNotFoundError:
    print("I do not know you favorite number yet!")
else:
    print("You favorite number is : " + numbers)
