def score(list_of_cards):
    score = 0
    for card in list_of_cards:
        score += score + card
    return score

import  random
cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Value for J, Q K = 10.
# A value can be 1 or 11.

your_cars_list = random.choices(cards_list, k=2)
computer_card_list = random.choices(cards_list, k=2)
computer_first_choice = computer_card_list[0]

print(f"Your cards: {your_cars_list}. current score: {print(score(your_cars_list))}")
print(f"Computer's first card: {computer_first_choice}")
choice = input("Type 'y' to get another card, type 'n' to pass: ")

if choice.lower() == 'y':
    your_cars_list.append(random.choice(cards_list))
    print(f"Your final hand: {your_cars_list}. final score: {print(score(your_cars_list))}")
else:
    print(f"Your final hand: {your_cars_list}")
    computer_card_list.append(computer_first_choice)
    if len(computer_card_list) < 2:
        computer_card_list.append(random.choice(cards_list))
    print(f"Computer's final hand: {computer_card_list}")
