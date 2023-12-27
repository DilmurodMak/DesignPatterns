from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
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

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


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

    def undo(self):
        self.garageDoor.down()


class GarageDoorCloseCommand(Command):
    def __init__(self, garageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.down()

    def undo(self):
        self.garageDoor.up()


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

    def undo(self):
        self.stereo.off()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()


class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        self.location = location
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH
        print(f"{self.location} ceiling fan is on high")

    def medium(self):
        self.speed = self.MEDIUM
        print(f"{self.location} ceiling fan is on medium")

    def low(self):
        self.speed = self.LOW
        print(f"{self.location} ceiling fan is on low")

    def getSpeed(self):
        return self.speed

    def off(self):
        self.speed = self.OFF
        print(f"{self.location} ceiling fan is off")


class CeilingFanHighCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.high()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()


class CeilingFanLowCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0

    def execute(self):
        self.ceilingFan.low()
        self.prevSpeed = self.ceilingFan.getSpeed()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()


class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.OFF:
            self.ceilingFan.off()


class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()


class NoCommand(Command):
    def execute(self):
        print("No command assigned")

    def undo(self):
        pass


class RemoteControl:
    def __init__(self):
        self.onCommands = [NoCommand() for _ in range(7)]
        self.offCommands = [NoCommand() for _ in range(7)]
        self.undoCommand = NoCommand()

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoButtonWasPushed(self):
        self.undoCommand.undo()

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
    fan = CeilingFan("Living Room")

    partyOnMacro = MacroCommand(
        [
            LightOnCommand(light),
            StereoOnWithCDCommand(stereo),
            CeilingFanHighCommand(fan),
        ]
    )
    partyOffMacro = MacroCommand(
        [LightOffCommand(light), StereoOffCommand(stereo), CeilingFanOffCommand(fan)]
    )

    remote.setCommand(0, LightOnCommand(light), LightOffCommand(light))
    remote.setCommand(
        1, GarageDoorOpenCommand(garageDoor), GarageDoorCloseCommand(garageDoor)
    )
    remote.setCommand(2, StereoOnWithCDCommand(stereo), StereoOffCommand(stereo))
    remote.setCommand(3, CeilingFanHighCommand(fan), CeilingFanOffCommand(fan))
    remote.setCommand(4, CeilingFanMediumCommand(fan), CeilingFanOffCommand(fan))
    remote.setCommand(5, partyOnMacro, partyOffMacro)

    remote.onButtonWasPushed(0)
    remote.offButtonWasPushed(0)

    print(str(remote))
    remote.undoButtonWasPushed()
    remote.offButtonWasPushed(0)
    remote.onButtonWasPushed(0)
    print(str(remote))
    remote.undoButtonWasPushed()

    remote.onButtonWasPushed(1)
    remote.offButtonWasPushed(1)

    remote.onButtonWasPushed(2)
    remote.offButtonWasPushed(2)

    remote.onButtonWasPushed(3)
    remote.onButtonWasPushed(4)
    remote.undoButtonWasPushed()
    remote.offButtonWasPushed(3)

    remote.onButtonWasPushed(5)
    remote.offButtonWasPushed(5)
