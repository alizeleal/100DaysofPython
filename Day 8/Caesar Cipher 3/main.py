# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(text,shift,direction):
    original_text = ""
    for letter in text:
        if letter in alphabet:
            if direction == "encode":
                shifted_position = alphabet.index(letter) + shift
            else:
                shifted_position = alphabet.index(letter) - shift
            shifted_position %= len(alphabet)
            original_text += alphabet[shifted_position]
        else:
            original_text+=letter

    print(f"Here is the {direction}d result: {original_text}")
    go_again = input("Type 'yes' if you want to do it again. Otherwise, press Enter.\n").lower()
    if go_again == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text,shift,direction)




# TODO-3: Can you figure out a way to restart the cipher program?


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


caesar(text, shift, direction)



