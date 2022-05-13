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

resto1 = Restaurant('baton rouge', 'steakhouse')

print("\n")
resto1.restaurant_open()
resto1.describe_restaurant()
print(resto1.number_served)

resto1.set_number_served(0)
resto1.increment_number_served(1)
resto1.increment_number_served(2)
resto1.increment_number_served(3)
resto1.increment_number_served(4)
resto1.increment_number_served(5)
print(f"The restaurant has served {resto1.number_served} meals")