
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit  - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
   
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

while True:
    temperature = (input('Enter the temperature to convert:'))
    
    try: 
        temperature = float(temperature)

        type = input('Is this temperature in Celsius or Fahrenheit? (C/F):')

        if type == 'C':
            print(f'{temperature}°C is {convert_to_fahrenheit(temperature)}°F')
        elif type == 'F':
                print(f'{temperature}°F is {convert_to_celsius(temperature)}°C')
        else:
                print("Sorry, you didn't enter C or F") 

    except:
        print('Invalid temperature. Please enter a numeric value')
