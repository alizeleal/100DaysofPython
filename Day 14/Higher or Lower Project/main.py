import random
import art
import game_data

print(art.logo)

counter = 0
option_a = random.choice(game_data.data)
option_b = random.choice(game_data.data)

def higher_lower(op_a, op_b, count):
    correct = True
    while correct:
        if op_a == op_b:
            op_b = random.choice(game_data.data)
        print(f"Compare A: {op_a["name"]}, a {op_a["description"]} from {op_a["country"]}.\n\n")
        print(art.vs)
        print(f"Against B: {op_b["name"]}, a {op_b["description"]} from {op_b["country"]}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if op_a["follower_count"] > op_b["follower_count"]:
            correct_option = "a"
            op_a = op_b
        else:
            correct_option = "b"
        if guess == correct_option:
            count += 1
            print(f"You are correct! Current score is {count}")
            print("\n"*20)
            print(art.logo)
            higher_lower(op_a, random.choice(game_data.data), count)
            return correct
        else:
            print(f"You are wrong! Game ended with score: {count}.  ")
            correct = False
            return correct

higher_lower(option_a, option_b, counter)
