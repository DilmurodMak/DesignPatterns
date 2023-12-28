# Home theatre facade with all sub systems


class Amplifier:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name, "amplifier is on")

    def off(self):
        print(self.name, "amplifier is off")

    def set_dvd(self, dvd):
        print(self.name, "amplifier is set to", dvd.name)

    def set_surround_sound(self):
        print(self.name, "amplifier is set to surround sound")

    def set_volume(self, volume):
        print(self.name, "amplifier volume is set to", volume)


class Tuner:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name, "tuner is on")

    def off(self):
        print(self.name, "tuner is off")

    def set_frequency(self, frequency):
        print(self.name, "tuner frequency is set to", frequency)

    def set_am(self):
        print(self.name, "tuner is set to AM")

    def set_fm(self):
        print(self.name, "tuner is set to FM")


class DvdPlayer:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name, "DVD player is on")

    def off(self):
        print(self.name, "DVD player is off")

    def eject(self):
        print(self.name, "DVD player is eject")

    def pause(self):
        print(self.name, "DVD player is pause")

    def play(self, movie):
        print(self.name, "DVD player is play", movie)

    def set_surround_audio(self):
        print(self.name, "DVD player is set surround audio")

    def set_two_channel_audio(self):
        print(self.name, "DVD player is set two channel audio")

    def stop(self):
        print(self.name, "DVD player is stop")


class CdPlayer:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name, "CD player is on")

    def off(self):
        print(self.name, "CD player is off")

    def eject(self):
        print(self.name, "CD player is eject")

    def pause(self):
        print(self.name, "CD player is pause")

    def play(self, cd):
        print(self.name, "CD player is play", cd)

    def stop(self):
        print(self.name, "CD player is stop")


class Projector:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name, "projector is on")

    def off(self):
        print(self.name, "projector is off")

    def tv_mode(self):
        print(self.name, "projector is in tv mode")

    def wide_screen_mode(self):
        print(self.name, "projector is in wide screen mode")


class TheaterLights:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name, "theater ceiling lights are on")

    def off(self):
        print(self.name, "theater ceiling lights are off")

    def dim(self, level):
        print(self.name, "theater ceiling lights are dimmed to", level, "%")


class Screen:
    def __init__(self, name):
        self.name = name

    def up(self):
        print(self.name, "screen is up")

    def down(self):
        print(self.name, "screen is down")


class PopcornPopper:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name, "popcorn popper is on")

    def off(self):
        print(self.name, "popcorn popper is off")

    def pop(self):
        print(self.name, "popcorn popper is popping popcorn")


class HomeTheaterFacade:
    def __init__(
        self,
        amp: Amplifier,
        tuner: Tuner,
        dvd: DvdPlayer,
        cd: CdPlayer,
        projector: Projector,
        screen: Screen,
        lights: TheaterLights,
        popper: PopcornPopper,
    ):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.light = lights
        self.popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.turn_on_movie_mode()
        self.popper.pop()
        self.screen.down()
        self.projector.wide_screen_mode()
        self.amp.set_dvd(self.dvd)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.turn_off_movie_mode()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

    def listen_to_cd(self, cd):
        print("Get ready for an audiophile experience...")
        self.turn_on_audio_mode()
        self.amp.set_dvd(self.cd)
        self.amp.set_surround_sound()
        self.cd.play(cd)

    def end_cd(self):
        print("Shutting down CD...")
        self.turn_off_audio_mode()
        self.cd.eject()
        self.cd.off()

    def turn_on_movie_mode(self):
        self.popper.on()
        self.light.off()  # Assuming lights off during movie mode
        self.projector.on()

    def turn_off_movie_mode(self):
        self.popper.off()
        self.light.on()  # Assuming lights on after movie mode
        self.screen.up()
        self.projector.off()
        self.amp.off()

    def turn_on_audio_mode(self):
        self.light.on()
        self.amp.on()
        self.amp.set_volume(5)

    def turn_off_audio_mode(self):
        self.amp.off()


if __name__ == "__main__":
    amp = Amplifier("Top-O-Line Amplifier")
    tuner = Tuner("Top-O-Line AM/FM Tuner")
    dvd = DvdPlayer("Top-O-Line DVD Player")
    cd = CdPlayer("Top-O-Line CD Player")
    projector = Projector("Top-O-Line Projector")
    screen = Screen("Theater Screen")
    lights = TheaterLights("Theater Ceiling Lights")
    popper = PopcornPopper("Popcorn Popper")

    home_theater = HomeTheaterFacade(
        amp, tuner, dvd, cd, projector, screen, lights, popper
    )
    home_theater.watch_movie("Raiders of the Lost Ark")
    home_theater.end_movie()
    home_theater.listen_to_cd("Dark Side of the Moon")
    home_theater.end_cd()
