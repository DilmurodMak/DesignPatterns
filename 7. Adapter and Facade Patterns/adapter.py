class Duck:
    def quack(self):
        pass

    def fly(self):
        pass


class Turkey:
    def gobble(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I am flying a short distance")


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()


class DuckAdapter(Turkey):
    def __init__(self, duck: Duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        self.duck.fly()


class DuckTestDrive:
    def main(self):
        duck = MallardDuck()
        turkey = WildTurkey()
        turkeyAdapter = TurkeyAdapter(turkey)
        duckAdapter = DuckAdapter(duck)

        print("The turkey says...")
        turkey.gobble()
        turkey.fly()

        print("\nThe duck says...")
        self.testDuck(duck)

        print("\nThe turkeyAdapter says...")
        self.testDuck(turkeyAdapter)

        print("\nThe duckAdapter says...")
        self.testTurkey(duckAdapter)

    def testDuck(self, duck: Duck):
        duck.quack()
        duck.fly()

    def testTurkey(self, turkey: Turkey):
        turkey.gobble()
        turkey.fly()


if __name__ == "__main__":
    DuckTestDrive().main()
