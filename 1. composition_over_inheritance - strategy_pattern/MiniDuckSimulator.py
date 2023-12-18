# get Duck, MallardDuck, FlyWithWings, FlyNoWay, Quack, MuteQuack
from MallardDuck import MallardDuck
from RocketDuck import RocketDuck

if __name__ == "__main__":
    # Create a MallardDuck with default behaviors
    mallard_duck = MallardDuck()
    # Display and perform initial behaviors
    mallard_duck.display()
    mallard_duck.perform_fly()  # Should display flying with wings
    mallard_duck.perform_quack()  # Should display quacking

    # Create a RocketDuck with default behaviors
    rocket_duck = RocketDuck()
    # Display and perform initial behaviors
    rocket_duck.display()
    rocket_duck.perform_fly()  # Should display rocket-powered flying
    rocket_duck.perform_quack()  # Should display rocket sound