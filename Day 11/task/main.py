import random
import art
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

def draw():
    """Draw a card from the list \n
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]"""
    return random.choice(cards)

def blackjack():
    """Blackjack Game"""
    print(art.logo)
    print("Welcome to Blackjack!")
    play = input("Press Enter to start playing\n")
    players_hand = []
    dealers_hand = []
    #first draws
    players_hand.append(draw())
    players_hand.append(draw())
    dealers_hand.append(draw())

    # draw first card
    if players_hand[-1] == 11 and sum(players_hand) > 21:
        players_hand.remove(11)
        players_hand.append(1)
    print(f"Your current cards are: {players_hand}, scoring {sum(players_hand)}")
    print(f"The Dealer's first card: {dealers_hand}")
    if sum(players_hand) == 21 and len(players_hand) == 2:
        print(f"Your cards are: {players_hand}")
        print("You've hit a Blackjack!")
        play = input("Type 'y' and press Enter to play again\n")
        if play == 'y':
            print("\n" * 50)
            blackjack()
        else:
            return False
    another_card = input("Type 'y' to draw another card. Type 'n' to pass.")
    while another_card == 'y':
        players_hand.append(draw())
        if players_hand[-1] == 11 and sum(players_hand) > 21:
            players_hand.remove(11)
            players_hand.append(1)
        print(f"Your current cards are: {players_hand}, scoring {sum(players_hand)}")
        print(f"The Dealer's first card: {dealers_hand}")

        if sum(players_hand) > 21:
            print("\n********----------********")
            print(f"Your final hand: {players_hand}, final score: {sum(players_hand)}")
            print(f"The Dealer's final hand: {dealers_hand}, final score: {sum(dealers_hand)}")
            print("\n\n(ㆆ _ ㆆ)\n\n")
            print("You overdraw. You lose!")
            print("********----------********\n")
            play = input("Type 'y' and press Enter to play again\n")
            if play == 'y':
                print("\n" * 50)
                blackjack()
            else:
                return False
        else:
            another_card = input("\nType 'y' to draw another card. Type 'n' to pass.\n")

    print(f"\nYour final hand: {players_hand}, final score: {sum(players_hand)}")
    dealers_hand.append(draw())
    while sum(dealers_hand) < 18:
        dealers_hand.append(draw())
        if dealers_hand[-1] == 11 and sum(dealers_hand) > 21:
            dealers_hand.remove(11)
            dealers_hand.append(1)
    print(f"\nThe Dealer's final hand: {dealers_hand}, final score: {sum(dealers_hand)}")
    if sum(dealers_hand) > 21:
        print("\n\n	☜(⌒▽⌒)☞\n\n")
        print("The dealer overdrawn! You win!")
    elif sum(players_hand) < sum(dealers_hand):
        print("\n\n(ㆆ _ ㆆ)\n\n")
        print("You lose!")
    elif sum(players_hand) > sum(dealers_hand):
        print("\n\n	☜(⌒▽⌒)☞\n\n")
        print("You won!")
    else:
        print("\n\n	(╥﹏╥)\n\n")
        print("It's a draw!")
    print("********----------********")
    play = input("Type 'y' and press Enter to play again\n")
    if play == 'y':
        print("\n"*50)
        blackjack()
    else:
        return False

blackjack()
