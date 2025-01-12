#!/bin/python3

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function for user interaction
if __name__ == "__main__":
    try:
        # Prompt the user to enter a temperature and its unit
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform the appropriate conversion
        if unit == "F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp:.1f}°F is {converted_temp:.1f}°C")
        elif unit == "C":
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp:.1f}°C is {converted_temp:.1f}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")

