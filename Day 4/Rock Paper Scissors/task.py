import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper and Scissors!")
hand_ascii = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n  "))
pull = random.choice([0,1,2])

if choice == 0:
    print("You've chosen: Rock")
    print(hand_ascii[choice])
elif choice == 1:
    print("You've chosen: Paper")
    print(hand_ascii[choice])
elif choice == 2:
    print("You've chosen: Scissors")
    print(hand_ascii[choice])
else:
    print("You didn't follow the rules")

if choice != "" and -1 < choice < 3:
    if pull == 0:
        print("The computer chose: Rock")
        print(hand_ascii[pull])
    elif pull == 1:
        print("The computer chose: Paper")
        print(hand_ascii[pull])
    else:
        print("The computer chose: Scissors")
        print(hand_ascii[pull])

if choice == pull:
    print("Try again.")

if choice==0:
    if pull == 1:
        print ("You lose.")
    if pull == 2:
        print("You win.")

if choice == 1:
    if pull == 2:
        print("You lose.")
    if pull == 0:
        print("You win.")

if choice == 2:
    if pull == 0:
        print("You lose.")
    if pull == 1:
        print("You win.")

