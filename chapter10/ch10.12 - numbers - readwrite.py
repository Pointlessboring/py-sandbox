import json

filename = 'favorite_number.txt'

try:
    with open(filename, 'r') as f:
        number = f.read()
except FileNotFoundError:
    print("I do not know you favorite number yet!")
    number = input("What is your favorite number? ")

    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print("You favorite number is : " + number)
