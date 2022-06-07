favorite_places = {
    'stefano': {
        'name': 'stefano',
        'fav1': 'rome',
        'fav2': 'faienca',
        'fav3': 'florence',
    },

    'martin':{
        'name': 'martin',
        'fav1': 'paris',
        'fav2': 'quimper',
    },

    'sebastien':{
        'name': 'sebastien',
        'fav1': 'montpellier',
    },
}

for people, people_info in favorite_places.items():
       
    name = people_info['name']
    fav1 = people_info.get('fav1')
    fav2 = people_info.get('fav2', '')
    fav3 = people_info.get('fav3', '')
    print(f"{name.title()}'s favorite places are: {fav1.title()} {fav2.title()} {fav3.title()}")
        