# Przelicznik temperatur

class TemperatureConverter:
    def __init__(self, temperature, scale):
        self.temperature = temperature
        self.scale = scale

    def to_celsius(self):
        if self.scale.lower() == 'fahrenheit':
            return (self.temperature - 32) * 5.0/9.0
        elif self.scale.lower() == 'kelvin':
            return self.temperature - 273.15
        else:
            return self.temperature

    def to_fahrenheit(self):
        if self.scale.lower() == 'celsius':
            return self.temperature * 9.0/5.0 + 32
        elif self.scale.lower() == 'kelvin':
            return (self.temperature - 273.15) * 9.0/5.0 + 32
        else:
            return self.temperature

    def to_kelvin(self):
        if self.scale.lower() == 'celsius':
            return self.temperature + 273.15
        elif self.scale.lower() == 'fahrenheit':
            return (self.temperature - 32) * 5.0/9.0 + 273.15
        else:
            return self.temperature


if __name__ == "__main__":
    temp = TemperatureConverter(32, 'Fahrenheit')
    print(f'32 Fahrenheit to Celsius: {temp.to_celsius()}')
    print(f'32 Fahrenheit to Kelvin: {temp.to_kelvin()}')
