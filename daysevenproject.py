import random as r 
from hangman_words import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
words = ['apple', 'banana', 'orange']

secWord = r.choice(word_list)

intro = []
endGame = False

count = len(secWord)
introCount = count

from hangman_art import logo
print(logo)
# insert art 
print('Welcome to Hangman!')
for underscore in secWord:
    intro += '_'


while not endGame:
    guess = input('Guess a letter.\n').lower()
    if guess in intro:
        print(f"You've already guessed {guess}")

    for position in range(len(secWord)):
         letter = secWord[position]
         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
         if letter == guess:
            intro[position] = letter
    if guess not in secWord:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            break
    print(f"{' '.join(intro)}")



    if "_" not in intro:
        endGame = True
        print("You win.")


    print(stages[lives])