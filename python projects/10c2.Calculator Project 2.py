def calculate(n1, n2, op):
    result = 0
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    else:
        print("Choose correct operation.")
    print(f"{n1} {op} {n2} = {result}")
    return result

def calculator_app():
    repeat = True

    num1 = float(input("Enter first number: "))

    while repeat:
        print("+\n-\n*\n/")
        operation = input("Pick the operation: ")
        if operation not in ['+', '-','*','/']:
            print('Wrong operation selected. Start Over..')
            calculator_app()
        else:
            num2 = float(input("Enter the next number: "))
            output = calculate(num1, num2, operation)
            choice = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start over. ")
            if choice.lower() == 'y':
                num1 = output
            elif choice.lower() == 'n':
                repeat = False
                calculator_app()
            else:
                print("Sorry, wrong choice.")


calculator_app()