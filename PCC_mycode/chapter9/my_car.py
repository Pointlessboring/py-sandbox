from car import Car    
    
my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying value directly thru an instance
print("\n")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying value thru a method
print("\n")
my_new_car.update_odometer(51)
my_new_car.read_odometer()

# Modifying value thru a method
print("\n")
my_new_car.update_odometer(35)
my_new_car.read_odometer()

# Modifying value thru a method
print("\n")
my_new_car.increment_odometer(3)
my_new_car.read_odometer()

# Modifying value thru a method
print("\n")
my_new_car.increment_odometer(-2)
my_new_car.read_odometer()
