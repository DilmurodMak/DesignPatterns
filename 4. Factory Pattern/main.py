from abc import ABC, abstractmethod


# Abstract Pizza
class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        for topping in self.toppings:
            print(f"   {topping}")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")


# Concrete Pizza Products
class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese"]


class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese", "Pepperoni"]


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Cheese Pizza"
        self.dough = "Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese"]

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese", "Pepperoni"]

    def bake(self):
        print("Bake for 35 minutes at 350")

    def cut(self):
        print("Cutting the pizza into square slices")


# Abstract PizzaStore
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
            return "Error: Invalid type of pizza"


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return "Error: Invalid type of pizza"


# Client
if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    print("Ordering NY Style Cheese Pizza")
    ny_store.order_pizza("cheese")

    print("Ordering Chicago Style Pepperoni Pizza")
    chicago_store.order_pizza("pepperoni")
