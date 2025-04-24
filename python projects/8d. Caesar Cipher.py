def caesar_cipher(encode_decode, original_message, shift_number):
    import string

    alphabet_list = list(string.ascii_lowercase)

    output_message = ''

    if encode_decode.lower() == 'decode':
        shift_number = shift_number * -1

    for letter in original_message.lower():
        if letter not in alphabet_list:
            output_message += letter
        else:
            index_id = alphabet_list.index(letter)
            shifted_index_id = index_id + shift_number
            shifted_index_id = shifted_index_id % len(alphabet_list) # to avoid index out of range error.
            output_message += alphabet_list[shifted_index_id]

    print(f"Your {encode_decode}d message is: {output_message}")


repeat = True

while repeat == True:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(encode_decode=choice, original_message=message, shift_number=shift)

    yes_no = input("Enter 'yes' if you want to go again. Otherwise, enter 'no.'\n")
    if yes_no.lower() == 'no':
        repeat = False

