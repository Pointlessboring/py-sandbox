toppings = []

prompt = "\nWhat topping would you like to add to your pizza?"
prompt += "\n(enter 'quit' to finish or 'list' to view current choices): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    elif topping == 'list':
        print(f"Current choices are: {toppings}")
    else:
        print(f"Adding {topping.title()} to your pizza.")
        toppings.append(topping.title())

print(f"Now preparing your pizza topped with {toppings}")