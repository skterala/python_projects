height = int(input("Enter your height: "))

if height >= 120:
    age = int(input("Enter Your Age: "))
    photo = input("Do you want to take a Photo? Yes or No: ")
    if age <= 12:
        amt = 5
    elif age <= 18:
        amt = 7
    elif age <= 22:
        amt = 10
    else:
        amt = 12

    if photo.lower() == 'yes':
        amt += 3
    print(f"Please pay ${amt}")
else:
    print("Sorry, you cannot ride the rollercoaster.")