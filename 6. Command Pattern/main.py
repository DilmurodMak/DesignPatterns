from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def __init__(self, location):
        self.location = location

    def on(self):
        print(f"{self.location} light is on")

    def off(self):
        print(f"{self.location} light is off")


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class GarageDoor:
    def up(self):
        print("Garage Door is Open")

    def down(self):
        print("Garage Door is Closed")


class GarageDoorOpenCommand(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.up()


class GarageDoorCloseCommand(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.down()


class Stereo:
    def on(self):
        print("Stereo is on")

    def off(self):
        print("Stereo is off")


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()


class CeilingFan:
    def on(self):
        print("Ceiling fan is on")

    def off(self):
        print("Ceiling fan is off")


class CeilingFanOnCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.ceilingFan.on()


class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.ceilingFan.off()


class NoCommand(Command):
    def execute(self):
        print("No command assigned")


class RemoteControl:
    def __init__(self):
        self.onCommands = [NoCommand() for _ in range(7)]
        self.offCommands = [NoCommand() for _ in range(7)]

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()

    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()

    def __str__(self):
        result = "\n------ Remote Control ------\n"
        for i in range(len(self.onCommands)):
            result += (
                f"[Slot {i}] "
                f"{str(self.onCommands[i].__class__.__name__)}  "
                f"{str(self.offCommands[i].__class__.__name__)}\n"
            )
        return result


if __name__ == "__main__":
    remote = RemoteControl()
    light = Light("Living Room")
    garageDoor = GarageDoor()
    stereo = Stereo()
    fan = CeilingFan()

    remote.setCommand(0, LightOnCommand(light), LightOffCommand(light))
    remote.setCommand(1, GarageDoorOpenCommand(garageDoor), GarageDoorCloseCommand(garageDoor))
    remote.setCommand(2, StereoOnWithCDCommand(stereo), StereoOffCommand(stereo))
    remote.setCommand(3, CeilingFanOnCommand(fan), CeilingFanOffCommand(fan))

    print(str(remote))

    remote.onButtonWasPushed(0)
    remote.offButtonWasPushed(0)

    remote.onButtonWasPushed(1)
    remote.offButtonWasPushed(1)

    remote.onButtonWasPushed(2)
    remote.offButtonWasPushed(2)

    remote.onButtonWasPushed(3)
    remote.offButtonWasPushed(3)
