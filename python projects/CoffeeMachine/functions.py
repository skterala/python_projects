import menu

def is_resource_sufficient(drink):
    """Returns True if the enough resources are available, otherwise returns False."""
    for item in menu.MENU[drink]["ingredients"]:
        if menu.resources[item] < menu.MENU[drink]["ingredients"][item]:
            print(f"Sorry there is not enough {item}")
            return False

    return True


def process_coins():
    """Takes the coins - Quarters, Dimes, Nickles and Pennies from the user and calculates the total amount."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def process_transaction(user_amount, drink):
    """Checks if the inserted coins are enough to make the drink or not.
       If User inserted more coins, returns the change.
       Adds the amount to the Profit.
    """
    drink_amount = float(menu.MENU[drink]["cost"])
    if user_amount < drink_amount:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    elif user_amount >= drink_amount:
        menu.profit += drink_amount
        change = round(user_amount - drink_amount, 2)
        if change > 0:
            print(f"Here is ${change} Dollars in change.")
        return True


def deduct_resources(drink):
    """After making the drink, deducts the ingredients quantity from resources dictionary."""
    for item in menu.MENU[drink]["ingredients"]:
        available = menu.resources[item]
        needed_for_drink = menu.MENU[drink]["ingredients"][item]
        remaining = available - needed_for_drink
        menu.resources[item] = remaining


