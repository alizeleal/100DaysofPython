import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.


# TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
#  If lives goes down to 0 then the game should stop and it should print "You lose."



# TODO-3: - print the ASCII art from 'stages'
#  that corresponds to the current number of 'lives' the user has remaining.
import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.



chosen_word = list(random.choice(word_list))
hang_word =""
for l in range(len(chosen_word)):
    hang_word +="_"
print(hang_word)
hang_word = list(hang_word)

print(stages[-1])
lives = 6
i=0
while i < len(chosen_word) and lives > 0:
    letter_guess = input("Make a guess? type a letter in lowercase")
    aux = 0
    for l in range(len(chosen_word)):
        if chosen_word[l] == letter_guess:
            print("Right")
            i += 1
            hang_word[l] = letter_guess
            aux += 1
        else:
            print("Wrong")

    if aux == 0:
        lives-=1
    print(stages[lives])

    print(''.join(hang_word))


if hang_word == chosen_word:
    print(f"A palavra era {''.join(chosen_word)}. Você ganhou!")
else:
    print(f"A palavra era {''.join(chosen_word)}. Você perdeu")

