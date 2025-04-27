def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Add these 4 functions into a dictionary as the values. Keys should be "+, -, *, /"

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    repeat = True

    num1 = float(input("What is the first number?: "))

    while repeat == True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over. ")

        if choice.lower() == 'y':
            num1 = answer
        elif choice.lower() == 'n':
            repeat = False
            print("\n" * 20)
            calculator()  # Call the same function again to reset from start.
        else:
            print("Sorry, wrong input is provided.")

calculator()