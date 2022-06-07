from pickle import TRUE


cars = ['bmw', 'audi', "toyota", 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', "toyota", 'subaru']
print("\nHere is the original list:")
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

print("\nHere is the original list in reverse order:")
cars.reverse()
print(cars)

print(f"\nThe list contains {len(cars)} cars in it.")