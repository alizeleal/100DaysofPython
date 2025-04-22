import random

import art

keep_playing = 'y'
def number_game():
    print(art.logo)
    print("Can you guess the number I'm thinking between 1 and 100?")
    secret_number = random.randrange(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    lives = 0
    if difficulty == "easy":
        lives += 10
    else:
        lives += 5

    while lives > 0:
        print(f"You have {lives} attempts to guess correctly.")
        guess = int(input("Make a guess: "))
        if guess > secret_number:
            print("Too high")
            lives -= 1
        elif guess < secret_number:
            print("Too low")
            lives -= 1
        else:
            print(f"You guessed right! The number is: {guess}")
            return
    if lives == 0:
        print("You didn't guess the correct number")

while keep_playing == 'y':
    number_game()
    keep_playing = input("Want to play again? Type 'y' to continue, press Enter to finish.")