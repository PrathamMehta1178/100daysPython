import random as r 
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

tie = '''
 _   _      
| | (_)     
| |_ _  ___ 
| __| |/ _ |
| |_| |  __/
 \__|_|\___|
'''

print('Welcome to Rock, Paper  Scissiors.\nType 0 for Rock, 1 for Paper, 2 for Scissors.')

choice = int(input())

if choice == 0:
    print(rock+'\nYou chose Rock!')

elif choice == 1:
    print(paper+'\nYou chose Paper!')
else:
    print(scissors+'You chose Scissiors!')

compMove = r.randint(0,3)

if compMove == 0:
    print(rock+'\nThe computer chose Rock!')

elif compMove == 1:
    print(paper+'\nThe computer chose Paper!')
else:
    print(scissors+'The computer chose Scissiors!')

if choice == compMove:
    print(tie+'It\'s a tie!')

elif choice == 0 and compMove == 1:
    print('The computer wins!')
elif choice == 0 and compMove == 2:
    print('You won!')

elif choice == 1 and compMove == 0:
    print('You won!')

elif choice == 1 and compMove == 2:
    print('The computer wins!')

elif choice == 2 and compMove == 1:
    print('You won!')

else:
    print('The computer wins!')






