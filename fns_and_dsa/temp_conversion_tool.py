
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # Ask the user for temperature
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
        elif unit == "F":
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")
        else:
            print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

