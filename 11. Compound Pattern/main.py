# factory pattern
class AbstractDuckFactory:
    def create_mallard_duck(self):
        pass

    def create_redhead_duck(self):
        pass

    def create_duck_call(self):
        pass

    def create_rubber_duck(self):
        pass


class AbstractGooseFactory:
    def create_goose(self):
        pass


class DuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedheadDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()


class GooseFactory(AbstractGooseFactory):
    def create_goose(self):
        return Goose()


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self):
        return QuackCounter(RedheadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())


# observer pattern - observable interface
class QuackObservable:
    def register_observer(self, observer):
        pass

    def notify_observers(self):
        pass


# observer gets notified when the subject changes
class Observer:
    def update(self, duck):
        pass


# quackable interface
class Quackable(QuackObservable):
    def quack(self):
        pass


class Observable(QuackObservable):
    def __init__(self, duck):
        self.observers = []
        self.duck = duck

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        if self.duck:
            for observer in self.observers:
                observer.update(self.duck)


class Quackologist(Observer):
    def update(self, duck):
        print("Quackologist: " + str(duck) + " just quacked.")


class MallardDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Quack")
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class RedheadDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Quack")
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class DuckCall(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Kwak")
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class RubberDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def quack(self):
        print("Squeak")
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class Goose:
    def honk(self):
        print("Honk")


# adapter pattern
class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.observable = Observable(self)
        self.goose = goose

    def quack(self):
        self.goose.honk()
        self.notify_observers()

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


# decorator pattern
class QuackCounter(Quackable):
    number_of_quacks = 0

    def __init__(self, duck):
        self.observable = Observable(self)
        self.duck = duck

    def quack(self):
        self.duck.quack()
        QuackCounter.number_of_quacks += 1
        self.notify_observers()

    @staticmethod
    def get_quacks():
        return QuackCounter.number_of_quacks

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def __str__(self):
        return str(self.duck)


class Flock(Quackable):
    def __init__(self):
        self.quackers = []

    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()

    def __str__(self):
        return "Flock of Quackers"


class DuckSimulator:
    def simulate(self, duckfactory):
        mallard_duck = duckfactory.create_mallard_duck()
        redhead_duck = duckfactory.create_redhead_duck()
        duck_call = duckfactory.create_duck_call()
        rubber_duck = duckfactory.create_rubber_duck()
        goose_duck = GooseAdapter(Goose())

        print("\nDuck Simulator: With Observer")

        # Register Quackologist as an observer for each duck
        quackologist = Quackologist()
        mallard_duck.register_observer(quackologist)
        redhead_duck.register_observer(quackologist)
        duck_call.register_observer(quackologist)
        rubber_duck.register_observer(quackologist)
        goose_duck.register_observer(quackologist)

        # flock of ducks
        flock_of_ducks = Flock()
        flock_of_ducks.add(mallard_duck)
        flock_of_ducks.add(redhead_duck)
        flock_of_ducks.add(duck_call)
        flock_of_ducks.add(rubber_duck)
        flock_of_ducks.add(goose_duck)

        # flock of mallards
        flock_of_mallards = Flock()
        mallard_one = duckfactory.create_mallard_duck()
        mallard_two = duckfactory.create_mallard_duck()
        mallard_three = duckfactory.create_mallard_duck()
        mallard_four = duckfactory.create_mallard_duck()

        # Register Quackologist as an observer for each mallard duck
        mallard_one.register_observer(quackologist)
        mallard_two.register_observer(quackologist)
        mallard_three.register_observer(quackologist)
        mallard_four.register_observer(quackologist)

        flock_of_mallards.add(mallard_one)
        flock_of_mallards.add(mallard_two)
        flock_of_mallards.add(mallard_three)
        flock_of_mallards.add(mallard_four)

        # Register Quackologist as an observer for the flock of ducks
        flock_of_ducks.register_observer(quackologist)

        # add flock of mallards to flock of ducks
        flock_of_ducks.add(flock_of_mallards)

        self.simulate_duck(flock_of_ducks)

        print("\nThe ducks quacked " + str(QuackCounter.get_quacks()) + " times")

    def simulate_duck(self, duck):
        duck.quack()


if __name__ == "__main__":
    simulator = DuckSimulator()
    duckfactory = CountingDuckFactory()
    simulator.simulate(duckfactory)
