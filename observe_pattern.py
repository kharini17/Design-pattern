# Observer interface
class Observer:
    def update(self, data):
        pass

# Concrete Observer
class Display(Observer):
    def update(self, data):
        print(f"Display updated with data: {data}")

# Subject interface
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)

# Concrete Subject
class WeatherMonitoringSystem(Subject):
    def __init__(self):
        super().__init__()
        self._weather_data = None

    def set_weather_data(self, data):
        self._weather_data = data
        self.notify_observers(data)

# Usage
weather_system = WeatherMonitoringSystem()
display = Display()

weather_system.add_observer(display)
weather_system.set_weather_data("Temperature: 22°C, Humidity: 60%")
