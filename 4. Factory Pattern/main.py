from abc import ABC, abstractmethod


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
    def prepare(self):
        print("Preparing NY Style Cheese Pizza")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class NYStylePepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing NY Style Pepperoni Pizza")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class ChicagoStyleCheesePizza(Pizza):
    def prepare(self):
        print("Preparing Chicago Style Cheese Pizza")

    def bake(self):
        print("Bake for 40 minutes at 350")

    def cut(self):
        print("Cutting the pizza into square slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


class ChicagoStylePepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Chicago Style Pepperoni Pizza")

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
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            raise ValueError("Error: Invalid type of pizza")


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            raise ValueError("Error: Invalid type of pizza")


# Client
if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    print("Ordering NY Style Cheese Pizza")
    ny_store.order_pizza("cheese")

    print("Ordering Chicago Style Pepperoni Pizza")
    chicago_store.order_pizza("pepperoni")
