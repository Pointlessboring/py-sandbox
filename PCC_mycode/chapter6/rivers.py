rivers = {
    'nil': 'egypt', 
    'mississipi': 'usa',
     'st-lawrence': 'canada',
     'seine': 'france',
     'danube': 'germany', 
     'volga': 'russia',
     'rubicon': 'italy'}

    
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")