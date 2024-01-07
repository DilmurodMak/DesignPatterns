from abc import ABC, abstractmethod


class MenuItem:
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


class PancakeHouseMenuIterator(Iterator):
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


class DinerMenuIterator(Iterator):
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


class CafeMenuIterator(Iterator):
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


class PancakeHouseMenu:
    def __init__(self):
        self.menu_items = []
        self.add_item(
            "K&B's Pancake Breakfast",
            "Pancakes with scrambled eggs, and toast",
            True,
            2.99,
        )
        self.add_item(
            "Regular Pancake Breakfast",
            "Pancakes with fried eggs, sausage",
            False,
            2.99,
        )
        self.add_item(
            "Blueberry Pancakes",
            "Pancakes made with fresh blueberries",
            True,
            3.49,
        )
        self.add_item(
            "Waffles",
            "Waffles, with your choice of blueberries or strawberries",
            True,
            3.59,
        )

    def add_item(self, name, description, vegetarian, price):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self):
        return CafeMenuIterator(self.menu_items)

    def remove_item(self, name):
        for i, item in enumerate(self.menu_items):
            if item.get_name() == name:
                self.menu_items.pop(i)
                break


class DinerMenu:
    def __init__(self):
        self.menu_items = []
        self.add_item(
            "Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True,
            2.99,
        )
        self.add_item("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.add_item(
            "Soup of the day",
            "Soup of the day, with a side of potato salad",
            False,
            3.29,
        )
        self.add_item(
            "Hotdog",
            "A hot dog, with sauerkraut, relish, onions, topped with cheese",
            False,
            3.05,
        )

    def add_item(self, name, description, vegetarian, price):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)

    def remove_item(self, name):
        for i, item in enumerate(self.menu_items):
            if item.get_name() == name:
                self.menu_items.pop(i)
                break


class CafeMenu(MenuItem):
    def __init__(self):
        self.menu_items = []
        self.add_item(
            "Veggies Burger andAir Fries",
            "Veggies burger on a whole wheat bun, lettuce, tomato, and fries",
            True,
            3.99,
        )
        self.add_item(
            "Soup of the day",
            "A cup of the soup of the day, with a side salad",
            False,
            3.69,
        )
        self.add_item(
            "Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            True,
            4.99,
        )

    def add_item(self, name, description, vegetarian, price):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self):
        return CafeMenuIterator(self.menu_items)

    def remove_item(self, name):
        for i, item in enumerate(self.menu_items):
            if item.get_name() == name:
                self.menu_items.pop(i)
                break


class Waitress:
    def __init__(self, pancake_house_menu, diner_menu, cafe_menu):
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu
        self.cafe_menu = cafe_menu

    def print_menu(self):
        pancake_house_menu_iterator = self.pancake_house_menu.create_iterator()
        diner_menu_iterator = self.diner_menu.create_iterator()
        cafe_menu_iterator = self.cafe_menu.create_iterator()

        print("MENU\n----\nBREAKFAST")
        self.__print_menu(pancake_house_menu_iterator)
        print("\nLUNCH")
        self.__print_menu(diner_menu_iterator)
        print("\nDINNER")
        self.__print_menu(cafe_menu_iterator)

    def __print_menu(self, iterator):
        while iterator.has_next():
            menu_item = iterator.next()
            print(
                menu_item.get_name(),
                ", ",
                menu_item.get_price(),
                " -- ",
                menu_item.get_description(),
            )


if __name__ == "__main__":
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    cafe_menu = CafeMenu()
    waitress = Waitress(pancake_house_menu, diner_menu, cafe_menu)
    waitress.print_menu()

    pancake_house_menu.remove_item("Waffles")
    print("\nAfter removing Waffles from the Breakfast Menu:")
    waitress.print_menu()
