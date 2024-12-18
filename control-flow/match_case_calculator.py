# A simple calculator

# Prompt the user for the input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sign = input("Choose the operation (+, -, *, /): ")

def calculate(num1, num2, sign):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operand"

# Call the function and print the result
result = calculate(num1, num2, sign)
print(result)


