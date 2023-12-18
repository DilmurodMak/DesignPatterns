# QuackBehavior interface
class QuackBehavior:
    def quack(self):
        pass


# Concrete implementation of quacking
class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


# Concrete implementation of mute quacking
class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


# Concrete implementation of squeaking
class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class RocketSound(QuackBehavior):
    def quack(self):
        print("Zoom Zoom!")
