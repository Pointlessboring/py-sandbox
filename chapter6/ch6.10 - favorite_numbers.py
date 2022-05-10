from curses import doupdate


favorite_numbers = {'ann': [7], 'stephane': [888], 'eric': [150], 'julia': [1, 2, 23], "chantale": [2, 55]}

for data in favorite_numbers:
    print(f"{data.title()}'s favorite number(s) are: {favorite_numbers[data]}")
    