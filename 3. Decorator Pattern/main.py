# Coffee Shop Example
from enum import Enum


class Size(Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


# Component
class Beverage:

    def __init__(self):
        self._description = "Unknown Beverage"
        self.size = Size.TALL

    def description(self):
        return self._description

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def cost(self):
        pass


# Concrete Component (Coffee)
class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "House Blend Coffee"

    def cost(self):
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Dark Roast Coffee"

    def cost(self):
        return 0.79


# Decorator
class CondimentDecorator(Beverage):
    def __init__(self, coffee, discount_rate=0):
        super().__init__()
        self.coffee = coffee
        self.discount_rate = discount_rate

    def description(self):
        return self.coffee.description()

    def set_size(self, size):
        self.coffee.set_size(size)

    def get_size(self):
        return self.coffee.get_size()

    def cost(self):
        return self.coffee.cost()


# Concrete Decorator
class Milk(CondimentDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def description(self):
        return self.coffee.description() + ", Milk"

    def cost(self):
        return self.coffee.cost() + 0.20 + self._calculate_condiment_cost(0.10)

    def _calculate_condiment_cost(self, base_cost):
        size_multiplier = {
            Size.TALL: 0.10,
            Size.GRANDE: 0.15,
            Size.VENTI: 0.20,
        }
        return base_cost * size_multiplier.get(self.get_size(), 0)


class Whip(CondimentDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def description(self):
        return self.coffee.description() + ", Whip"

    def cost(self):
        return self.coffee.cost() + 0.10 + self._calculate_condiment_cost(0.10)

    def _calculate_condiment_cost(self, base_cost):
        size_multiplier = {
            Size.TALL: 0.10,
            Size.GRANDE: 0.15,
            Size.VENTI: 0.20,
        }
        return base_cost * size_multiplier.get(self.get_size(), 0)


class Soy(CondimentDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def description(self):
        return self.coffee.description() + ", Soy"

    def cost(self):
        return self.coffee.cost() + 0.15 + self._calculate_condiment_cost(0.10)

    def _calculate_condiment_cost(self, base_cost):
        size_multiplier = {
            Size.TALL: 0.10,
            Size.GRANDE: 0.15,
            Size.VENTI: 0.20,
        }
        return base_cost * size_multiplier.get(self.get_size(), 0)


class Mocha(CondimentDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def description(self):
        return self.coffee.description() + ", Mocha"

    def cost(self):
        return self.coffee.cost() + 0.15 + self._calculate_condiment_cost(0.10)

    def _calculate_condiment_cost(self, base_cost):
        size_multiplier = {
            Size.TALL: 0.10,
            Size.GRANDE: 0.15,
            Size.VENTI: 0.20,
        }
        return base_cost * size_multiplier.get(self.get_size(), 0)


class Discount(CondimentDecorator):
    def __init__(self, coffee, discount_rate):
        super().__init__(coffee, discount_rate)
        self.discount_rate = discount_rate

    def description(self):
        return (
            "Discount: "
            + str(self.discount_rate * 100)
            + "%"
        )

    def cost(self):
        return self.coffee.cost() * (1 - self.discount_rate)


if __name__ == "__main__":
    # double mocha soy whip espresso
    coffee = Espresso()
    coffee.set_size(Size.GRANDE)
    coffee = Mocha(coffee)
    coffee = Mocha(coffee)
    coffee = Soy(coffee)
    coffee = Whip(coffee)
    cost = round(coffee.cost(), 2)
    print(f"{coffee.description()} ({coffee.get_size().name}) - ${cost}")

    # dark roast with double mocha and whip
    coffee = DarkRoast()
    coffee.set_size(Size.TALL)
    coffee = Mocha(coffee)
    coffee = Mocha(coffee)
    coffee = Whip(coffee)
    cost = round(coffee.cost(), 2)
    print(f"{coffee.description()} ({coffee.get_size().name}) - ${cost}")

    # house blend with soy, mocha, and whip and 10% discount
    coffee = HouseBlend()
    coffee.set_size(Size.VENTI)
    coffee = Soy(coffee)
    coffee = Mocha(coffee)
    coffee = Whip(coffee)
    cost = round(coffee.cost(), 2)
    print(f"{coffee.description()} ({coffee.get_size().name}) - ${cost}")
    coffee = Discount(coffee, 0.1)
    cost = round(coffee.cost(), 2)
    print(f"{coffee.description()} ({coffee.get_size().name}) - ${cost}")
