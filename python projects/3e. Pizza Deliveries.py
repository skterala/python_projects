print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if pepperoni.lower() == 'y':
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese.lower() == 'y':
    bill += 1

print(f"Your final bill is ${bill}")
