import random
import string

# Create numbers list from 0 to 9
num_list = []

for num in range(0, 10):
    num_list.append(num)

# print(num_list)

# Create letters list with lower case and capital letters.
letter_list = list(string.ascii_letters)

# print(letter_list)

# Create symbols list.
symbols_list = ['~','`','!','@','#','$','%','^','&','*','<','>','.','?','/']

# print(symbols_list)

print('Welcome to the PyPassword Generator!')
total_len = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

# number of letters that are needed
remaining_chars = total_len - symbols - numbers

# Create a password with letters, numbers and symbols.
password = ''

for _ in range(1, symbols + 1):
    password += random.choice(symbols_list) # Pick the random symbol from the list.

for _ in range(1, numbers + 1):
    password += str(random.choice(num_list)) # Pick the random number from the list.

for _ in range(1, remaining_chars + 1):
    password += random.choice(letter_list) # Pick the random letter from the list.

# Convert password string to list for shuffle.

pwd_list = list(password) # Convert to list.
random.shuffle(pwd_list) # shuffle the list.

# Convert from list to string.
password = ''.join(pwd_list)

print(f"Your new password is: {password}")