import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list

chosen_word = random.choice(word_list)
print(chosen_word)

place_holder = ''

for _ in chosen_word:
    place_holder += "_"

print(place_holder)

# Ask the user to guess a letter and assign their answer to a variable calles guess. Make guess lowercase.

game_over = False
guesses_letters_list = []


while game_over == False:
    guess = input("Guess a letter: ").lower()

    # Check if the letter that user guessed is one of the letters in the chosen_word. Print "Right: if it is, "Wrong" if it is not.
    display = ''

    for l in chosen_word:
        if l == guess:
            display += l
            guesses_letters_list.append(l)
        elif l in guesses_letters_list:
            display += l
        else:
            display += '_'

    print(display)

    if '_' not in display:
        game_over = True
        print("You Win.")


