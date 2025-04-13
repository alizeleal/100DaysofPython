import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# easy version

password_suggestion =""
auxiliary_arrow = []
for i in range(0,nr_letters):
    auxiliary_arrow = random.choice(letters)
    password_suggestion = password_suggestion + auxiliary_arrow

for i in range(0,nr_symbols):
    auxiliary_arrow = random.choice(symbols)
    password_suggestion = password_suggestion + auxiliary_arrow

for i in range(0, nr_numbers):
    auxiliary_arrow = random.choice(numbers)
    password_suggestion = password_suggestion + auxiliary_arrow



# hard version
#include a shuffle

hard_password = list(password_suggestion)
random.shuffle(hard_password)

print("This is a simple password suggestion")
print(password_suggestion)

print("This is a harder password suggestion")

print(''.join(hard_password))