from abc import ABC, abstractmethod
from enum import Enum

class PizzaSize(Enum):
    large = "large"
    small = "small"
    medium = "medium"

# Step 1: Base interface

class PizzaInterface(ABC):
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def size(self):
        pass

# Step 2: Concrete Pizza

class Pizza(PizzaInterface):
    def __init__(self, size, amount):
        self._size = size
        self._amount = amount

    def price(self):
        return self._amount

    def size(self):
        return self._size

# Step 3: Decorator Base Class

class PizzaDecorator(PizzaInterface):
    def __init__(self, pizza: PizzaInterface):
        self._pizza = pizza

    def price(self):
        return self._pizza.price()

    def size(self):
        return self._pizza.size()

# Step 4: Concrete Decorator (Toppings)

class Toppings(PizzaDecorator):
    def price(self):
        return self._pizza.price() + 10

# Step 5: Usage

pizza1 = Pizza("medium", 400)
pizza_with_toppings = Toppings(pizza1)

print("Pizza price is :", pizza_with_toppings.price())
print("Pizza size is :", pizza_with_toppings.size())
