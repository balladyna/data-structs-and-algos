# Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively
# represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should include methods for setting the value
# of each type, and retrieving the value of each type.


class Flower:
    def __init__(self, name, petals, price):
        self._name = name
        self._petals = 0
        self._price = 0.0

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price


my_flower = Flower('Daisy', 10, 1.49)

print(my_flower.get_name())

