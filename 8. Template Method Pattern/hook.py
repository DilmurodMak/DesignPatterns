class CaffaineBeverageWithHook:
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def brew(self):
        pass

    def add_condiments(self):
        pass

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    def customer_wants_condiments(self):
        return True


class CoffeeWithHook(CaffaineBeverageWithHook):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

    def customer_wants_condiments(self):
        answer = self.getUserInput()
        if answer.lower().startswith("y"):
            return True
        else:
            return False

    def getUserInput(self):
        answer = None
        print("Would you like milk and sugar with your coffee (y/n)?")
        try:
            answer = input()
        except IOError:
            print("IOError trying to read your answer")
        if answer is None:
            return "no"
        return answer


class TeaWithHook(CaffaineBeverageWithHook):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

    def customer_wants_condiments(self):
        answer = self.getUserInput()
        if answer.lower().startswith("y"):
            return True
        else:
            return False

    def getUserInput(self):
        answer = None
        print("Would you like lemon with your tea (y/n)?")
        try:
            answer = input()
        except IOError:
            print("IOError trying to read your answer")
        if answer is None:
            return "no"
        return answer


if __name__ == "__main__":
    coffee = CoffeeWithHook()
    tea = TeaWithHook()
    print("Making coffee...")
    coffee.prepare_recipe()
    print("Making tea...")
    tea.prepare_recipe()
