# Multiplication Table Generator

number = int(input("Enter a number to see its multiplication table:"))

for i in range(1, 11): # range include 1 to 10
    print(f"{number} * {i} = {number * i}") # print the multiplication result
