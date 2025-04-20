'''
Rules:
======
Rock beats Scissors (Rock crushes Scissors)
Scissors beats Paper (Scissors cuts Paper)
Paper beats Rock (Paper covers Rock)
If both players choose the same shape, it's a tie.

'''
import random

rpsc = ["Rock ✊", "Paper ✋", "Scissors ✌️"]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
user_choice = rpsc[user_input]
computer_choice = rpsc[random.randint(0,2)]

if user_choice == computer_choice:
    print(f"User Choice: {user_choice} and Computer Choice: {computer_choice}. It's a tie!")
else:
    if user_choice == 'Rock ✊' and computer_choice == 'Paper ✋':
        print(f"User Choice: {user_choice} and Computer Choice: {computer_choice}. You lose!")
    elif user_choice == 'Paper ✋' and computer_choice == 'Scissors ✌️':
        print(f"User Choice: {user_choice} and Computer Choice: {computer_choice}. You lose!")
    elif user_choice == 'Scissors ✌️' and computer_choice == 'Rock ✊':
        print(f"User Choice: {user_choice} and Computer Choice: {computer_choice}. You lose!")
    else:
        print(f"User Choice: {user_choice} and Computer Choice: {computer_choice}. You Win!")