# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius using global conversion factor.
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    Returns:
        float: Temperature in Celsius
    """
    try:
        celsius = (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return round(celsius, 2)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit using global conversion factor.
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    try:
        fahrenheit = 32 + float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR
        return round(fahrenheit, 2)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    """Main program loop for temperature conversion."""
    while True:
        try:
            # Get temperature and unit from user
            temp = input("\nEnter temperature (or 'q' to quit): ")
            if temp.lower() == 'q':
                print("Goodbye!")
                break
                
            unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()
            
            # Validate unit input
            if unit not in ['C', 'F']:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue
            
            # Perform conversion based on input unit
            if unit == 'C':
                fahrenheit = convert_to_fahrenheit(temp)
                print(f"{temp}°C = {fahrenheit}°F")
            else:
                celsius = convert_to_celsius(temp)
                print(f"{temp}°F = {celsius}°C")
                
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("Welcome to the Temperature Converter!")
    print("This program converts temperatures between Celsius and Fahrenheit.")
    main()
