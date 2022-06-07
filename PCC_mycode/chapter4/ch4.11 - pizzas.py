pizzas = ['pepperoni', 'all-dressed', 'vegetarian', 'tomato']
friend_pizzas = pizzas[:]

pizzas.append("cheese")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
