'''
age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}")

# Here, if we provide the age in letters, we will get ValueError. To fix this, use try/exception clause.
'''

# identify which part of the code is causing the error.
# in the above example, when the user enters the age in letters, converting string to an Int is causing ValueError.
# In the except clause, add what kind of error you are getting. Ex: ValueError.

try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed invalid number. Enter the age in numbers, like 15.")
    age = int(input("How old are you? "))

if age > 18:
      print(f"You can drive at age {age}")