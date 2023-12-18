# Weather Station Example
# Observer Interface
class Observer:
    def update(self, temperature, humidity, pressure):
        pass


# Subject Interface
class Subject:
    def register(self, observer):
        pass

    def remove(self, observer):
        pass

    def notify(self):
        pass


# Display Element Interface
class Display(Observer):
    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify()


class CurrentConditionsDisplay(Display):
    # display current data from WeatherData object
    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.weather_data = weather_data
        weather_data.register(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(
            "Current conditions: {}F degrees and {}% humidity".format(
                self.temperature, self.humidity
            )
        )


class StaticDisplay(Display):
    def __init__(self, weather_data):
        self.temperature = []
        self.humidity = []
        self.pressure = []
        self.weather_data = weather_data
        weather_data.register(self)
    
    def update(self, temperature, humidity, pressure):
        self.temperature.append(temperature)
        self.humidity.append(humidity)
        self.pressure.append(pressure)
        self.display()
    
    def display(self):
        avg_temp = sum(self.temperature) / len(self.temperature)
        avg_humidity = sum(self.humidity) / len(self.humidity)
        print(
            "Average conditions: {}F degrees and {}% humidity".format(
                avg_temp, avg_humidity
            )
        )


if __name__ == "__main__":
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    static_display = StaticDisplay(weather_data)
    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
