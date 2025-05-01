import functions
import menu

is_machine_on = True

menu.profit = 0

while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if choice == 'off':
        is_machine_on = False
    elif choice == 'report':
        print(f"Water: {menu.resources['water']}ml")
        print(f"Milk: {menu.resources['milk']}ml")
        print(f"Coffee: {menu.resources['coffee']}g")
        print(f"Money: ${menu.profit}")
    else:
        if functions.is_resource_sufficient(choice):
            user_amount = functions.process_coins()
            if functions.process_transaction(user_amount, choice):
                functions.deduct_resources(choice)
                print(f"Here is your {choice}. Enjoy!")

