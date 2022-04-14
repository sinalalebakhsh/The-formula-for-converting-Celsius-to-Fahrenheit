
def import_os():
    import os
    os.system('cls')
import_os()

# celsius to fahrenheit (32°C × 9/5) + 32 = 89.6°F
# Kelvin to fahrenheit (32K − 273.15) × 9/5 + 32 = -402.1°F
# Calender year to Day (multiply the time value by 365)

number = 28

def celsius_to_fahrenheit(number):
    num1 = number * 9.5
    return num1 + 32

def kelvin_to_fahrenheit(number):
    num1 = (number - 273.15) * 9.5
    return num1 + 32

def calender_to_day(number):
    return number * 365

print('Celsius to Fahrenheit: ',celsius_to_fahrenheit(number))
print('Kelvin  to Fahrenheit: ',kelvin_to_fahrenheit(number))
print('Calender  year to day: ',calender_to_day(number))
