pet1 = {
    'name': 'joey',
    'type': 'bird',
    'age': 4,
    'owner': 'luke',
}

pet2 = {
    'name': 'fido',
    'type': 'dog',
    'age': 2,
    'owner': 'john',
}

pet3 = {
    'name': 'charly',
    'type': 'lizard',
    'age': 3,
    'owner': 'anna',
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner'].title()}'s {pet['type'].title()} is {pet['age']} years old.")