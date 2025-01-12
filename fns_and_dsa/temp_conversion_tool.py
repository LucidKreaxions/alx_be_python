# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + OFFSET

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp:.1f}°C is {converted_temp:.1f}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp:.1f}°F is {converted_temp:.1f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

