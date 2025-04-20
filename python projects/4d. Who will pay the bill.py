import random

friends = ["Riddhish", "Ruthvik", "Simi", "Sarah", "Saurish", "Saanvi"]

# Option 1:
random_choice = random.choice(friends)
print(random_choice)

# Option 2:
print(friends[random.randint(0,5)])