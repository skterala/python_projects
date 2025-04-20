print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percent_tip = int(input("How much tip would you like to give? 10, 12, 05 15? "))
ppl = int(input("How many people to split the bill? "))
total_bill = bill * (1 + percent_tip/100)
each_person_amount = total_bill/ppl
print(f"Each person should pay: ${round(each_person_amount,2)}")