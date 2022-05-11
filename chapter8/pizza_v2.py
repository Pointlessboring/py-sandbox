def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a pizza with the following ingredients:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
