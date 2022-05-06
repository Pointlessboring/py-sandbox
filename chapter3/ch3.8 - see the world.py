#################
# EG 20220506
# Interesting little example

world_cities = ["Cape Town", "St-Petersburg", "Buenos Aires", "Istanbul", "Kyoto"]

print("1) Original list: ",world_cities)
print("2) Sorted original list: ",sorted(world_cities))
print("3) Original list: ",world_cities)
print("4) Sorted inversed original list: ",sorted(world_cities, reverse = True))
print("5) Original list: ",world_cities)
world_cities.reverse()
print("6) Reversed original list: ",world_cities)
world_cities.reverse()
print("7) Original list: ",world_cities)
world_cities.sort()
print("8) Original list sorted: ",world_cities)
world_cities.sort(reverse = True)
print("9) Original list sorted reverse: ",world_cities)