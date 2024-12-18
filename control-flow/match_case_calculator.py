# A simple calculator for practicing match-case

# prompt the user for the input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sign =  input("Choose the operation (+, -, *, /): ")

def calculate(sign):
    match sign:
        case +:
            return num1 + num2
        case -:
            return num1 - num2
        case *:
            return num1 * num2
        case /:
            return num1 / num2
        case -:
            return "Invalid operand"
print(sign)


