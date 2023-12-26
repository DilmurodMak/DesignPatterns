from abc import ABC, abstractmethod


# Pizza ingredient factory interface
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass


class Dough(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Sauce(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Cheese(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Clam(ABC):
    @abstractmethod
    def __str__(self):
        pass


class ThinCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"


class ThickCrustDough(Dough):
    def __str__(self):
        return "Thick Crust Dough"


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Plum Tomato Sauce"


class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"


class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Mozzarella Cheese"


class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"


class FrozenClam(Clam):
    def __str__(self):
        return "Frozen Clam"


class FreshClam(Clam):
    def __str__(self):
        return "Fresh Clam"


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_clam(self):
        return FreshClam()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_clam(self):
        return FrozenClam()


# Pizza Interfaces
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


# Concrete Pizza Products
class NYStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
        self.dough = None
        self.sauce = None
        self.cheese = None

    def prepare(self):
        print("Preparing NY Style Cheese Pizza")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()

        print(
            "Ingredients"
            + "\n"
            + str(self.dough)
            + "\n"
            + str(self.sauce)
            + "\n"
            + str(self.cheese)
        )

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
        self.dough = None
        self.sauce = None
        self.cheese = None

    def prepare(self):
        print("Preparing Chicago Style Cheese Pizza")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()

        print(
            "Ingredients"
            + "\n"
            + str(self.dough)
            + "\n"
            + str(self.sauce)
            + "\n"
            + str(self.cheese)
        )

    def bake(self):
        print("Bake for 40 minutes at 350")

    def cut(self):
        print("Cutting the pizza into square slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


# PizzaStore Interfaces
class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


# Concrete PizzaStores
class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == "cheese":
            return NYStyleCheesePizza(ingredient_factory)
        else:
            raise ValueError("Error: Invalid type of pizza")


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza(ingredient_factory)
        else:
            raise ValueError("Error: Invalid type of pizza")


# Client
if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    print("Ordering NY Style Cheese Pizza")
    ny_store.order_pizza("cheese")

    print("Ordering Chicago Style Cheese Pizza")
    chicago_store.order_pizza("cheese")
