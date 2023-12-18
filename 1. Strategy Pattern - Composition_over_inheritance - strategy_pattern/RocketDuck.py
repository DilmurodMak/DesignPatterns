from Duck import Duck
from FlyBehavior import RocketFly
from QuackBehavior import RocketSound


class RocketDuck(Duck):
    def __init__(self):
        super().__init__(RocketFly(), RocketSound())

    def display(self):
        print("I'm a Rocket Duck")