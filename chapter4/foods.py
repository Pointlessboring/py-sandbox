my_foods = ['pizza', 'falafel', 'cake']
friend_foods = my_foods[:] # if you remove the slice if they ARE the same list i.e. reference

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
