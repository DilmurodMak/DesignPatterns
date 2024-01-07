from abc import ABC, abstractmethod


# Component interface
class MenuComponent(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def is_vegetarian(self):
        pass

    @abstractmethod
    def add_item(self, menu_component):
        pass

    @abstractmethod
    def remove_item(self, menu_component):
        pass

    @abstractmethod
    def create_iterator(self):
        pass

    @abstractmethod
    def print_item(self):
        pass


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def add_item(self, menu_component):
        raise NotImplementedError("Cannot add item to MenuItem")

    def remove_item(self, menu_component):
        raise NotImplementedError("Cannot remove item from MenuItem")

    def create_iterator(self):
        raise NotImplementedError("Iterator not supported for MenuItem")

    def print_item(self):
        print(
            self.get_name(),
            ", ",
            self.get_price(),
            " -- ",
            self.get_description(),
        )


class Iterator(ABC):
    def __init__(self, menu_items):
        self.menu_items = menu_items
        self.position = 0

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def remove(self):
        pass


class CompositeIterator(Iterator):
    def has_next(self):
        return self.position < len(self.menu_items)

    def next(self):
        menu_item = self.menu_items[self.position]
        self.position += 1
        return menu_item

    def remove(self):
        if self.position <= 0:
            raise Exception(
                "You can't remove an item until you've done at least one next()"
            )
        if self.menu_items[self.position - 1] is not None:
            for i in range(self.position - 1, len(self.menu_items) - 1):
                self.menu_items[i] = self.menu_items[i + 1]
            self.menu_items[len(self.menu_items) - 1] = None


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_components = []

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        raise NotImplementedError("Price not applicable for Menu")

    def is_vegetarian(self):
        raise NotImplementedError("Vegetarian status not applicable for Menu")

    def add_item(self, menu_component):
        self.menu_components.append(menu_component)

    def remove_item(self, name):
        for menu_component in self.menu_components:
            if menu_component.get_name() == name:
                self.menu_components.remove(menu_component)
                return

    def create_iterator(self):
        return CompositeIterator(self.menu_components)

    def print_item(self):
        print(f"\n{self.get_name()}, {self.get_description()}")
        print("---------------------")

        for menu_component in self.menu_components:
            menu_component.print_item()


class PancakeHouseMenu(Menu):
    def __init__(self):
        super().__init__("Pancake House Menu", "Breakfast items")
        self.add_item(
            MenuItem(
                "K&B's Pancake Breakfast",
                "Pancakes with scrambled eggs, and toast",
                True,
                2.99,
            )
        )
        self.add_item(
            MenuItem(
                "Regular Pancake Breakfast",
                "Pancakes with fried eggs, sausage",
                False,
                2.99,
            )
        )
        self.add_item(
            MenuItem(
                "Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49
            )
        )
        self.add_item(
            MenuItem(
                "Waffles",
                "Waffles, with your choice of blueberries or strawberries",
                True,
                3.59,
            )
        )

    def create_iterator(self):
        return CompositeIterator(self.menu_components)

    def print_item(self):
        super().print_item()


class DinerMenu(Menu):
    def __init__(self):
        super().__init__("Diner Menu", "Lunch items")
        self.add_item(
            MenuItem(
                "Vegetarian BLT",
                "(Fakin') Bacon with lettuce & tomato on whole wheat",
                True,
                2.99,
            )
        )
        self.add_item(
            MenuItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        )
        self.add_item(
            MenuItem(
                "Soup of the day",
                "Soup of the day, with a side of potato salad",
                False,
                3.29,
            )
        )
        self.add_item(
            MenuItem(
                "Hotdog",
                "A hot dog, with sauerkraut, relish, onions, topped with cheese",
                False,
                3.05,
            )
        )

    def create_iterator(self):
        return CompositeIterator(self.menu_components)

    def print_item(self):
        super().print_item()


class CafeMenu(Menu):
    def __init__(self):
        super().__init__("Cafe Menu", "Dinner items")
        self.add_item(
            MenuItem(
                "Veggie Burger and Air Fries",
                "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
                True,
                3.99,
            )
        )
        self.add_item(
            MenuItem(
                "Soup of the day",
                "A cup of the soup of the day, with a side salad",
                False,
                3.69,
            )
        )
        self.add_item(
            MenuItem(
                "Burrito",
                "A large burrito, with whole pinto beans, salsa, guacamole",
                True,
                4.29,
            )
        )

    def create_iterator(self):
        return CompositeIterator(self.menu_components)

    def print_item(self):
        super().print_item()


class Waitress:
    def __init__(self, menus):
        self.menus = menus

    def print_menu(self):
        for menu in self.menus:
            iterator = menu.create_iterator()
            print(f"\n{menu.get_name()}\n----")
            self.__print_menu(iterator)

    def __print_menu(self, iterator):
        while iterator.has_next():
            menu_item = iterator.next()
            menu_item.print_item()


if __name__ == "__main__":
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    cafe_menu = CafeMenu()

    waitress = Waitress([pancake_house_menu, diner_menu, cafe_menu])
    waitress.print_menu()

    pancake_house_menu.remove_item("Waffles")
    print("\nAfter removing Waffles from the Breakfast Menu:")
    waitress.print_menu()
