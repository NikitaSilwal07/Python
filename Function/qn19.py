#19.Write a function temperature_conversion(celsius) that converts Celsius to Fahrenheit.

def temperature_conversion(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
celsius=32
print(f"{celsius} degree celsius is equal to {temperature_conversion(celsius)} degree fahrenheit.")