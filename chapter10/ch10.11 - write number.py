import json

number = input("What is your favorite number? " )
filename = 'favorite_number.txt'
with open(filename, 'w') as f:
    json.dump(number,f)
