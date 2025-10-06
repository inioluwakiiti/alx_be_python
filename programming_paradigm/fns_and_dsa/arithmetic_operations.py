def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations (add, subtract, multiply, divide).

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 
                         'multiply', or 'divide').

    Returns:
        float or str: The result of the operation as a float, or a string 
                      message if division by zero occurs.
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
        return num1 / num2
    else:
        return f"Invalid operation: {operation}"
