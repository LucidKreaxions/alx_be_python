# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Ensure the size is positive
if size > 0:
    # Initialize row counter
    row = 0
    
    # Draw the Pattern using a while loop
    while row < size:
        # Use a for loop to print asterisks in the current row
        for col in range(size):
            print("*", end="")
        
        # Move to the next line after finishing the row
        print()
        
        # Increment the row counter
        row += 1
else:
    print("Please enter a positive integer.")
