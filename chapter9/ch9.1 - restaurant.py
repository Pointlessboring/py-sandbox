class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name.title()} is proud to serve {self.type} cuisine to its customers.")
    
    def restaurant_open(self):
        print(f"\n{self.name.title()} is now open!")


resto1 = Restaurant('baton rouge', 'steakhouse')

print(resto1.name)
print(resto1.type)
print("\n")

resto1.restaurant_open()
resto1.describe_restaurant()
