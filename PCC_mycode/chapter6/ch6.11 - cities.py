cities = {
    'montreal': {
        'name': 'montreal',
        'pop': 2000000,
        'country': 'canada',
        'fact': 'mont-royal',
    },
    
    'toronto': {
        'name': 'toronto',
        'pop': 4000000,
        'country': 'canada',
        'fact': 'CN tower',
    },

    'paris': {
        'name': 'paris',
        'pop': 6000000,
        'country': 'france',
        'fact': 'eiffel tower',
    },
}

for key, data in cities.items():
        print(f"{data['name'].title()}, located in {data['country'].title()}, has a population of {data['pop']} and is known for the {data['fact'].title()}.")