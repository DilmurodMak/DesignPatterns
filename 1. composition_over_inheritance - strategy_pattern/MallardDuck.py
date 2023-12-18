from Duck import Duck
from FlyBehavior import FlyWithWings
from QuackBehavior import Quack


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("I'm a Mallard Duck")