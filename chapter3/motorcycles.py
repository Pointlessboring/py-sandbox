motorcycles = ['honda', 'yamaha', 'suzuki', 'harley davidson', 'Triumph', 'Kawasaki', 'Piaggio']
motorcycles.insert(4,'ducati')

print("\n")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('Triumph')
print(motorcycles)
print("\n")

last_owned = motorcycles.pop(1)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

last_owned = motorcycles.pop()
print(f"The first motorcycle I owned was a {last_owned.title()}.")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
print("\n")
