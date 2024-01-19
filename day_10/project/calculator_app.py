from art import logo


# Display
print(logo)

# Add
def add(n1, n2):
    """Takes two numbers and return the sum"""
    return n1 + n2

# Subtract
def subtract(n1, n2):
    """Takes two numbers and return the difference"""
    return n1 - n2

# Multiply
def multiply(n1, n2):
    """Takes two numbers and return the product"""
    return n1 * n2

# Divide
def divide(n1, n2):
    """Takes two number and return the quotient"""
    return n1 / n2

# Operations Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))

    # Print out operation symbols
    for symbol in operations:
        print(symbol)

    continue_calculating = True

    while continue_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
        if should_continue == "y":
            num1 = answer
        else:
            continue_calculating = False
            calculator()


calculator()

