class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.name.title()} is proud to serve {self.type} cuisine to its customers.")
    
    def restaurant_open(self):
        print(f"\n{self.name.title()} is now open!")


resto1 = Restaurant('baton rouge', 'steakhouse')
resto2 = Restaurant('Pizza Hut', 'american')
resto3 = Restaurant("La cuillère d'argent", 'French')

resto1.restaurant_open()
resto1.describe_restaurant()

resto2.restaurant_open()
resto2.describe_restaurant()

resto3.restaurant_open()
resto3.describe_restaurant()
