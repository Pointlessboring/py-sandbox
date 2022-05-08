requested_toppings = 'mushroom'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

# keeping the same variable name but changing type is bad form...

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("We are out of green peppers right now.")
    else: 
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#

#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("We are out of green peppers right now.")
        else: 
            print(f"Adding {requested_topping}.")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
