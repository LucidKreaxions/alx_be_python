def perform_operation(num1, num2, operation):
    """
    Perform an arithmetic operation based on the input parameters.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the arithmetic operation, or an error message for invalid inputs.
    """
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Invalid operation"