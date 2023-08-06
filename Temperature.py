def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

def celsius_to_kelvin(temp):
    return temp + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

def fahrenheit_to_kelvin(temp):
    return (temp + 459.67) * 5/9

def kelvin_to_fahrenheit(temp):
    return (temp * 9/5) - 459.67

def convert_temperature(temp, from_scale, to_scale):
    if from_scale == 'Celsius' and to_scale == 'Fahrenheit':
        return celsius_to_fahrenheit(temp)
    elif from_scale == 'Fahrenheit' and to_scale == 'Celsius':
        return fahrenheit_to_celsius(temp)
    elif from_scale == 'Celsius' and to_scale == 'Kelvin':
        return celsius_to_kelvin(temp)
    elif from_scale == 'Kelvin' and to_scale == 'Celsius':
        return kelvin_to_celsius(temp)
    elif from_scale == 'Fahrenheit' and to_scale == 'Kelvin':
        return fahrenheit_to_kelvin(temp)
    elif from_scale == 'Kelvin' and to_scale == 'Fahrenheit':
        return kelvin_to_fahrenheit(temp)
    else:
        return temp

temp = float(input("Enter temperature: "))
from_scale = input("Enter temperature scale (Celsius/Fahrenheit/Kelvin): ")
to_scale = input("Enter temperature scale to convert to (Celsius/Fahrenheit/Kelvin): ")

result = convert_temperature(temp, from_scale, to_scale)
print(f"{temp} {from_scale} = {result} {to_scale}")
