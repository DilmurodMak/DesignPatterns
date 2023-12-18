# FlyBehavior interface
class FlyBehavior:
    def fly(self):
        pass


# Concrete implementation of flying with wings
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying with wings")


# Concrete implementation of no flying
class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Unable to fly")


class RocketFly(FlyBehavior):
    def fly(self):
        print("Rocket-powered flying! Fire and smoke!")
