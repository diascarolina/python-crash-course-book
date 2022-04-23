from typing import List
from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors: List):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def list_flavors(self):
        print(self.flavors)

if __name__ == "__main__":
    ice_cream = IceCreamStand("Sorveteria", "Doces", ["chocolate", "morango"])
    ice_cream.list_flavors()