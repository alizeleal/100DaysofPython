print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Which direction do you want to take? Type left or right")

if direction == "right":
    print("You've found an angry dragon. Game over!")
elif direction=="left":
    print("It is raining the the road flooded. What do you do?")
    action = input("Type wait to wait until the water goes down; type swim if you swim to the other side of the road ")
    if action == "swim":
        print("The current is too strong and and you drowned. Game over!")
    elif action == "wait":
        print("Once the water went down, you see three doors.")
        door = input("Choose the door by the color: red, blue, yellow. Type your color choice")
        if door == "red" or door == "blue":
            print("A poisonous smoke hit your nostrils. Game over!")
        elif door != "yellow":
            print("You didn't follow the rules. Game over!")
        else:
            print("Congratulations! I've found the treasure")
    else:
        print("You didn't follow the rules. Game over!")
else:
    print("You didn't follow the rules. Game over!")



