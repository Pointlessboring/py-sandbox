class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name.title()} is proud to serve {self.type} cuisine to its customers.")
    
    def restaurant_open(self):
        print(f"\n{self.name.title()} is now open!")

    def set_number_served(self, value):
        """Method to set the number of customer served to a specific value"""
        if value >= 0:
            self.number_served = value
        else: 
            print("You cannot set the number of meals served to a negative number")

    def increment_number_served(self, value):
        """Method to increment the number of meals served by a specific number"""
        if value >= 0:
            self.number_served += value
        else: 
            print("You cannot update the number of meals by a negative number")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        self.type = "Ice Cream"

    def add_flavors(self, flavor):
        self.flavors.append(flavor)

    def describe_restaurant(self):
        print(f"{self.name.title()} is proud to serve {self.type} to its customers.")

