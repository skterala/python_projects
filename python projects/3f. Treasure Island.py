print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

left_or_right = input("You're at a cross road. Where do you want to go?\n    Type 'left' or 'right'\n")

if left_or_right.lower() == 'left':
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake.\n   Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if swim_or_wait.lower() == 'wait':
        door_color = input("You arrive at the island unharmed. There is a house with 3 doors.\n  One red, one yellow and one blue. Which color do you choose?\n")
        if door_color.lower() == 'red':
            print("Burned by fire.\n  Game Over.")
        elif door_color.lower() == 'blue':
            print("Eaten by beasts.\n  Game Over.")
        elif door_color.lower() == 'yellow':
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attached by trout.\n  Game Over.")
else:
    print("Fall into a hole.\n  Game Over.")