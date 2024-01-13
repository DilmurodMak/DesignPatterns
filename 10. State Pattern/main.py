import random


# State interface
class State:
    def insert_coin(self):
        pass

    def eject_coin(self):
        pass

    def turn_crank(self):
        pass

    def dispense(self):
        pass


# Concrete state classes
class SoldOutState(State):
    def insert_coin(self):
        print("Sorry, the machine is sold out.")

    def eject_coin(self):
        print("You can't eject, you haven't inserted a coin yet.")

    def turn_crank(self):
        print("You turned, but there are no gumballs.")

    def dispense(self):
        print("No gumball dispensed.")


class NoCoinState(State):
    def insert_coin(self):
        print("You inserted a coin.")
        gumball_machine.set_state(gumball_machine.get_has_coin_state())

    def eject_coin(self):
        print("You haven't inserted a coin.")

    def turn_crank(self):
        print("You turned, but there's no coin.")

    def dispense(self):
        print("You need to pay first.")


class HasCoinState(State):
    def insert_coin(self):
        print("You can't insert another coin.")

    def eject_coin(self):
        print("Coin returned.")
        gumball_machine.set_state(gumball_machine.get_no_coin_state())

    def turn_crank(self):
        print("You turned...")
        gumball_machine.set_state(gumball_machine.get_sold_state())

    def dispense(self):
        print("No gumball dispensed.")


class SoldState(State):
    def insert_coin(self):
        print("Please wait, we're already giving you a gumball.")

    def eject_coin(self):
        print("Sorry, you already turned the crank.")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        gumball_machine.release_ball()

        # 10% chance to dispense an additional gumball
        if random.random() < 0.1 and gumball_machine.get_count() > 0:
            print("Congratulations! You got an extra gumball for free!")
            gumball_machine.release_ball()

        if gumball_machine.get_count() > 0:
            gumball_machine.set_state(gumball_machine.get_no_coin_state())
        else:
            print("Oops, out of gumballs!")
            gumball_machine.set_state(gumball_machine.get_sold_out_state())


# Context class
class GumballMachine:
    def __init__(self, count):
        self.count = count
        self.sold_out_state = SoldOutState()
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.sold_state = SoldState()
        self.state = self.no_coin_state

    def set_state(self, state):
        self.state = state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_no_coin_state(self):
        return self.no_coin_state

    def get_has_coin_state(self):
        return self.has_coin_state

    def get_sold_state(self):
        return self.sold_state

    def insert_coin(self):
        self.state.insert_coin()

    def eject_coin(self):
        self.state.eject_coin()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self):
        print("A gumball comes rolling out the slot.")
        if self.count != 0:
            self.count -= 1

    def refill(self, count):
        self.count = count
        self.state = self.no_coin_state

    def get_count(self):
        return self.count

    def __str__(self):
        return f"Gumball Machine: {self.count}"


# Usage example
gumball_machine = GumballMachine(10)
print(gumball_machine)
for _ in range(10):
    gumball_machine.insert_coin()
    gumball_machine.turn_crank()
    print(gumball_machine)
