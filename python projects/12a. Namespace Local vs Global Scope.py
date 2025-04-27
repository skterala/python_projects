# Local and Global Scope

age = 10 # This is a Global scope variable. Any function, if, for, while loops can also use this variable
salary = 10000

def employee():
    age = 20   # This variable is local to the function
    print(f"Employee Age inside the function: {age}")
    print(f"Employee Salary is {salary}")  # salary variable is used within ths function even it was declared outside.


employee() # Calling the function.

print(f"Employee Age inside the function: {age}") # Print statement from Global variable

