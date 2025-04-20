'''
bmi is equal to the person's weight divided by the person's height squared.
'''

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight/(height ** 2)
print(f"Your BMI is {round(bmi,2)}")