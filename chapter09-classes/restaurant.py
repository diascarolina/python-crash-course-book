class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name: {self.restaurant_name}, Cuisine type: {self.cuisine_type}')

    def open_rastaurant(self):
        print(f'The restaurant "{self.restaurant_name}" is now open.')


if __name__ == "__main__":
    restaurant = Restaurant('Algum Nome', 'Algum Tipo')
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_rastaurant()