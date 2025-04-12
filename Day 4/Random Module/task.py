import random

# random_number = random.random() #random number from 0 to 1
# print(random_number)
#
# random_float = random.uniform(1,10) #random number considering uniform dist
# print(random_float)

guess = input("head of tail?\n")
chance = random.random()*10
if chance<=5 and guess == "head":
    print ("Head.\n"
           "You got it right!")
elif chance<=5 and guess == "tail":
    print ("Head.\n"
           "Better Luck next time.")
elif chance>=5 and guess == "tail":
    print ("Tail.\n"
           "You got it right!")
elif chance >= 5 and guess == "head":
        print("Tail.\n"
              "Better Luck next time.")
else:
    print("How many faces does your coins have?")

