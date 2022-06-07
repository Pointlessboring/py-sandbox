from restaurants import IceCreamStand

stand1 = IceCreamStand('VanillaCap', 'IceCreamStand')

print("\n")
stand1.restaurant_open()
stand1.describe_restaurant()
print(stand1.number_served)

stand1.set_number_served(0)
stand1.increment_number_served(1)
stand1.increment_number_served(2)
stand1.increment_number_served(3)
stand1.increment_number_served(4)
stand1.increment_number_served(5)
print(f"The restaurant has served {stand1.number_served} meals")