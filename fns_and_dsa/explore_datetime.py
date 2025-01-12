# To be continued: health-break.
from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time."""
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

def calculate_future_date(days):
    """Calculate a future date given a number of days to add."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

def main():
    # Part 1: Display the Current Date and Time
    display_current_datetime()

    # Part 2: Calculate a Future Date
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(days_to_add)
    print(f"Future date: {future_date}")

if __name__ == "__main__":
    main()
