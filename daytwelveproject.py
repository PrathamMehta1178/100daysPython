import random as r
guesses = 0
difficulty = input('Welcome to Guess a Number!\nWould you like hard or easy difficulty?\n').lower()

if difficulty[0] == 'e':
    guesses += 10
else:
    guesses += 5

number = r.randint(1, 100)

aguesses = guesses + 1

for i in range(aguesses):
    guess = int(input('Guess a number\n'))
    print(f'DEBUG answer = {number}')

    if guess == number:
        print('You guessed the right number!')
        break
    elif guess > number:
        print('Too high')
    elif guess < number:
        print('Too low' )
    if i == aguesses and guess != number:
        print('You failed.')
