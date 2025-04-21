import random

import art
print(art.logo)

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
players_hand =[]
dealers_hand = []

print("Welcome to Blackjack!")
play = input("Type y to start playing\n")
sum_player = 0
sum_dealer = 0

def draw():
    return random.choice(cards)

# while play == 'y':
player_draw = draw()
dealer_draw = draw()
another = 'y'

dealers_hand.append(dealer_draw)
players_hand.append(player_draw)
print(f"You drew {players_hand}")
print(f"The Dealer drew {dealers_hand}")

while another == 'y':
    for i in range(len(players_hand)):
        sum_player += players_hand[i]
        sum_dealer += dealers_hand[i]
    if sum_dealer < 21 and sum_dealer < 21:
        another = input("Want to draw another card? Type y to continue\n")
    if sum_dealer > 21:
        print(f"The dealer currently has: {dealers_hand}")
        print(f"You won! The dealer has reached {sum_dealer} points.")
        break
    elif sum_player > 21:
        print(f"You drew {players_hand}")
        print(f"You lose! Your score is {sum_player-21} above the limit of 21 points.")
        break
    else:
        sum_player = 0
        sum_dealer = 0
        player_draw = draw()
        players_hand.append(player_draw)
        for i in range(len(players_hand)):
            sum_player += players_hand[i]
        if sum_player > 21:
            print(f"You drew {players_hand}")
            print(f"You lose! Your score is {sum_player - 21} above the limit of 21 points.")
        elif sum_player == 21:
            print("You've reached 21 points! You won!")
        else:
            print(f"You drew {players_hand}")
        print(f"The dealer currently has: {dealers_hand}")
        dealer_draw = draw()
        dealers_hand.append(dealer_draw)
