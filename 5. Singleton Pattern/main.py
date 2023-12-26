import threading


class ChocolateBoiler:
    __unique_instance = None
    __lock = threading.Lock()

    def __init__(self):
        self.empty = True
        self.boiled = False

    @classmethod
    def get_instance(cls):
        if cls.__unique_instance is None:
            with cls.__lock:
                if cls.__unique_instance is None:
                    cls.__unique_instance = ChocolateBoiler()
        return cls.__unique_instance

    def fill(self):
        if self.empty:
            self.empty = False
            self.boiled = False
            print("Fill the boiler with a milk/chocolate mixture")

    def drain(self):
        if not self.empty and self.boiled:
            self.empty = True
            print("Drain the boiled milk and chocolate")

    def boil(self):
        if not self.empty and not self.boiled:
            self.boiled = True
            print("Bring the contents to a boil")

    def is_empty(self):
        return self.empty

    def is_boiled(self):
        return self.boiled


if __name__ == "__main__":
    boiler = ChocolateBoiler.get_instance()
    boiler.fill()
    boiler.boil()
    boiler.drain()
