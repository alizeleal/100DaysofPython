# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
bidders = {}
another_bidder = "yes"
bids = []

while another_bidder == "yes":
    print(art.logo)
    name = input("What's your name?\n")
    bid = float(input("Place your bid: $ "))
    bidders[name] = bid
    another_bidder = input("Are there any other bidders? Type 'yes or 'no'.\n")
    print("\n"*50)

def winning_bid(bets):
    winners_bid = 0
    for player in bets:
        bids.append(bets[player])
    for i in range(len(bets)):
        if bids[i] > winners_bid:
            winners_bid = bids[i]
    for player in bets:
        if bets[player] == winners_bid:
            print(art.logo)
            print(f"The winning bid was made by {player} with the value of $ {round(winners_bid,2)}")

winning_bid(bidders)




