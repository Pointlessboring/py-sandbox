person_1 = {'first_name': 'anna', 'last_name': 'bouchard', 'age': 24, 'city': 'New York'}
person_2 = {'first_name': 'bob', 'last_name': 'marley', 'age': 35, 'city': 'Los Angeles'}
person_3 = {'first_name': 'charles', 'last_name': 'taylord', 'age': 55, 'city': 'Miami'}

persons = [person_1, person_2, person_3]

for person in persons: 
    print(f"{person['first_name'].title()}'s last name is: {person['last_name'].title()}")
    print(f"{person['first_name'].title()}'s age is: {person['age']}")
    print(f"{person['first_name'].title()} lives in: {person['city'].title()}")
