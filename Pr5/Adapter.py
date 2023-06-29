# Существующий класс, который нужно адаптировать
class WeatherAPI:
    def get_temperature(self):
        return 25

    def get_humidity(self):
        return 70


# Целевой интерфейс, который ожидается клиентским кодом
class WeatherProvider:
    def get_temperature_celsius(self):
        pass

    def get_humidity_percent(self):
        pass


# Адаптер, преобразующий интерфейс WeatherAPI в WeatherProvider
class WeatherAdapter(WeatherProvider):
    def __init__(self, weather_api):
        self.weather_api = weather_api

    def get_temperature_celsius(self):
        temperature_fahrenheit = self.weather_api.get_temperature()
        temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
        return temperature_celsius

    def get_humidity_percent(self):
        return self.weather_api.get_humidity()


# Клиентский код
def main():
    weather_api = WeatherAPI()
    adapter = WeatherAdapter(weather_api)

    print("Temperature:", adapter.get_temperature_celsius(), "°C")
    print("Humidity:", adapter.get_humidity_percent(), "%")


if __name__ == '__main__':
    main()
