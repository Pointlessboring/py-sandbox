class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer value to a given value."""
        """Reject the change if it attemps to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else: 
            print("You can't roll back an odometer")
    
    
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
