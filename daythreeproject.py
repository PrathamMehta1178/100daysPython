print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************

''')

print('Welcome to Treasure Island.\nYour goal is to find the Treausre.\nYou\'re at a cross road. Left or Right?')
choice = input().lower()

if choice[0] == 'r':
    print('You fell into a hole. Game Over')
else:
    print('You arrive at a lake. There is an island in the middle. Do you swim across or wait for a boat?')
    choice = input().lower()

    if choice[0] == 's':
        print('You try to swim across the lake, but a group of piranhas attack you. Game Over')
    else:
        print('You wait until a boat arrives, and when it does, you ride it over to the island.\nWhen you arrive there is a house with three doors. Red, Blue, and Yellow.\nWhich one do you take?')
        choice = input().lower()

        if choice[0] == 'y':
            print('You found the treasure!\nYou win!')
        else:
            print('You chose the wrong door.\nYou lose.')