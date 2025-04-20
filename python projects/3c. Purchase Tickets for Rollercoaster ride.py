height = int(input("Enter your height: "))

if height >= 120:
    age = int(input("Enter Your Age: "))
    if age <= 12:
        print("Please pay $5 for your ticket.")
    elif age <= 18:
        print("Please pay $7 for your ticket.")
    elif age <= 22:
        print("Please pay $10 for your ticket.")
    else:
        print("Please pay $12 for your ticket.")
else:
    print("Sorry, you cannot ride the rollercoaster.")