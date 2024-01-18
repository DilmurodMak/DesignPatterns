import random


class GumballMachine:
    def __init__(self, location, count):
        self.location = location
        self.count = count
        self.state = NoCoinState(self)

    def set_state(self, state):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin()

    def eject_coin(self):
        self.state.eject_coin()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self):
        print("A gumball comes rolling out the slot.")
        if self.count > 0:
            self.count -= 1

    def refill(self, count):
        self.count = count
        self.set_state(NoCoinState(self))

    def get_count(self):
        return self.count

    def get_state(self):
        return str(self.state)

    def get_location(self):
        return self.location

    def __str__(self):
        return f"Gumball Machine: {self.count}"


class State:
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        pass

    def eject_coin(self):
        pass

    def turn_crank(self):
        pass

    def dispense(self):
        pass


class NoCoinState(State):
    def __str__(self):
        return "NoCoinState"

    def insert_coin(self):
        print("You inserted a coin.")
        self.gumball_machine.set_state(HasCoinState(self.gumball_machine))

    def eject_coin(self):
        print("You haven't inserted a coin.")

    def turn_crank(self):
        print("You turned, but there's no coin.")

    def dispense(self):
        print("You need to pay first.")


class HasCoinState(State):
    def __str__(self):
        return "HasCoinState"

    def insert_coin(self):
        print("You can't insert another coin.")

    def eject_coin(self):
        print("Coin returned.")
        self.gumball_machine.set_state(NoCoinState(self.gumball_machine))

    def turn_crank(self):
        print("You turned...")
        self.gumball_machine.set_state(SoldState(self.gumball_machine))

    def dispense(self):
        print("No gumball dispensed.")


class SoldState(State):
    def __str__(self):
        return "SoldState"

    def insert_coin(self):
        print("Please wait, we're already giving you a gumball.")

    def eject_coin(self):
        print("Sorry, you already turned the crank.")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            if random.random() < 0.1:
                self.gumball_machine.set_state(WinnerState(self.gumball_machine))
            else:
                self.gumball_machine.set_state(NoCoinState(self.gumball_machine))
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(SoldOutState(self.gumball_machine))


class SoldOutState(State):
    def __str__(self):
        return "SoldOutState"

    def insert_coin(self):
        print("Sorry, the machine is sold out.")

    def eject_coin(self):
        print("You can't eject, you haven't inserted a coin yet.")

    def turn_crank(self):
        print("You turned, but there are no gumballs.")

    def dispense(self):
        print("No gumball dispensed.")


class WinnerState(State):
    def __str__(self):
        return "WinnerState"

    def insert_coin(self):
        print("Please wait, we're already giving you a gumball.")

    def eject_coin(self):
        print("Sorry, you already turned the crank.")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        print(
            "Congratulations! You're a winner! You get two gumballs for the price of one."
        )
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() == 0:
            self.gumball_machine.set_state(SoldOutState(self.gumball_machine))
        else:
            self.gumball_machine.release_ball()
            if self.gumball_machine.get_count() > 0:
                self.gumball_machine.set_state(NoCoinState(self.gumball_machine))
            else:
                print("Oops, out of gumballs!")
                self.gumball_machine.set_state(SoldOutState(self.gumball_machine))


# Monitor class
class GumballMonitor:
    def __init__(self, gumball_machine_proxy):
        self.gumball_machine_proxy = gumball_machine_proxy

    def report(self):
        print(f"Gumball Machine: {self.gumball_machine_proxy.get_location()}")
        print(f"Current Gumballs: {self.gumball_machine_proxy.get_count()}")
        print(f"Current State: {self.gumball_machine_proxy.get_state()}")


# Proxy class
class GumballMachineProxy:
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_coin(self):
        self.gumball_machine.insert_coin()

    def eject_coin(self):
        self.gumball_machine.eject_coin()

    def turn_crank(self):
        self.gumball_machine.turn_crank()
        self.gumball_machine.dispense()

    def release_ball(self):
        self.gumball_machine.release_ball()

    def refill(self, count):
        self.gumball_machine.refill(count)

    def get_count(self):
        return self.gumball_machine.get_count()

    def get_location(self):
        return self.gumball_machine.get_location()

    def get_state(self):
        return self.gumball_machine.get_state()

    def __str__(self):
        return f"Gumball Machine ({self.get_location()}): {self.get_count()}, State: {self.get_state()}"


# Usage example
gumball_machine_austin = GumballMachine("Austin", 10)
gumball_machine_proxy_austin = GumballMachineProxy(gumball_machine_austin)
gumball_monitor_austin = GumballMonitor(gumball_machine_proxy_austin)

gumball_machine_boulder = GumballMachine("Boulder", 5)
gumball_machine_proxy_boulder = GumballMachineProxy(gumball_machine_boulder)
gumball_monitor_boulder = GumballMonitor(gumball_machine_proxy_boulder)

gumball_machine_newyork = GumballMachine("New York", 1)
gumball_machine_proxy_newyork = GumballMachineProxy(gumball_machine_newyork)
gumball_monitor_newyork = GumballMonitor(gumball_machine_proxy_newyork)

# Sample operations
gumball_machine_austin.insert_coin()
gumball_machine_austin.turn_crank()

gumball_machine_boulder.insert_coin()
gumball_machine_boulder.turn_crank()

gumball_machine_newyork.insert_coin()
gumball_machine_newyork.turn_crank()

# Reports
gumball_monitor_austin.report()
gumball_monitor_boulder.report()
gumball_monitor_newyork.report()
