class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

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
    
    def fill_gas_tank(self):
        """Method to fill the gas tank"""
        print("Gas tank has been filled")
        self.gas_tank = 100

    def read_tank_indicator(self):
        """Return the gas tank indicator level"""
        return self.gas_tank

class ElectricCar(Car):    
    """Represents aspects of a car, specific to electric vehicules."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement regarding the battery size."""
        print(f"The car has a {self.battery_size} kWh battery.")
    
    def fill_gas_tank(self):
        """Overrides the Super class method as we have no gas tank"""
        print("This car does not have a gas tank")


my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())
print(f"Gas tank level is at {my_new_car.read_tank_indicator()}%.")
my_new_car.fill_gas_tank()

print(f"Gas tank level is at {my_new_car.read_tank_indicator()}%.")

### Child class specific code

print("\n")
my_tesla = ElectricCar('tesla', 'model', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()