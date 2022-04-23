class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restaurant name: {self.restaurant_name}, Cuisine type: {self.cuisine_type}')

    def open_rastaurant(self):
        print(f'The restaurant "{self.restaurant_name}" is now open.')

    def set_number_served(self, number_of_clients):
        if number_of_clients >= self.number_served:
            self.number_served = number_of_clients
        else:
            print("You can't reduce this number.")
            
    def increment_number_served(self, increment):
        self.number_served += increment



if __name__ == "__main__":
    restaurant = Restaurant('Algum Nome', 'Algum Tipo')
    print(restaurant.number_served)
    restaurant.set_number_served(5)
    print(restaurant.number_served)
    restaurant.set_number_served(1)
    print(restaurant.number_served)
    restaurant.increment_number_served(10)
    print(restaurant.number_served)
