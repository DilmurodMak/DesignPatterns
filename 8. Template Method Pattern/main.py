class CaffaineBeverage:
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def brew(self):
        pass

    def add_condiments(self):
        pass

    def pour_in_cup(self):
        print("Pouring into cup")


class Tea(CaffaineBeverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")


class Coffee(CaffaineBeverage):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")


if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()
    print("Making tea...")
    tea.prepare_recipe()
    print("Making coffee...")
    coffee.prepare_recipe()
