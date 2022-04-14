
def import_os():
    import os
    os.system('cls')
import_os()

#(32°C × 9/5) + 32 = 89.6°F

def celsius_to_fahrenheit(celsius):
    num1 = celsius * 9.5
    return num1 + 32

print(celsius_to_fahrenheit(500))
