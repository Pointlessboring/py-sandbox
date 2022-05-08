from curses import doupdate


favorite_numbers = {'ann': 7, 'stephane': 888, 'eric':150, 'julia': 23, "chantale": 55}

for data in favorite_numbers:
    print(data, favorite_numbers[data])