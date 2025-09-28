#  Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors

FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    print("Temperature Conversion Tool")
    
    try:
        temperature = float(input("Enter the temperature to convert: "))
        cel_or_fah = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if cel_or_fah == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        elif cel_or_fah == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()