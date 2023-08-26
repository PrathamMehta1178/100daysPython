import random as r 

def checker(score):
    if score > 21:
        
        return True
    else:
        return False
def intro():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
    choice = input('Welcome to BlackJack!\nType \'S\' to start, \'E\' to exit, \'R\' for rules.\n').lower()
    if choice == 'r':
        print('Rules\nThe goal is to get to 21 or as close as possible.\nIf 21 is past, the game is over.\nYou will be dealt two cards. You can choose to recive another(hit) or keep your hand(stand)\nYou will only see the first card of the dealer\'s deck\nIf the dealer\'s deck is less than 17 they must draw another card.\n')
        intro()
    elif choice == 'e':
        print('Thanks for playing.')
    elif choice == 's':
        startGame()
    
def startGame():
    hit = True
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    playerDeck = []
    dealerDeck = []
    dscore = 0
    pscore = 0

    for i in range(2):
        playerDeck.append(cards[r.randint(0,12)])
    pscore = playerDeck[0] + playerDeck[1]
    
    
    while dscore < 17:
        dealerDeck.append(cards[r.randint(0,12)])
        dscore = dscore + dealerDeck[-1]

    if dscore > 21:
        print('You won! The dealer drew more than 21!')
        intro()
    else:
        pass
    
    
    print(f'Your deck is {playerDeck}. Current Score: {pscore}.')
    while hit:
        
        choice = input('Would you like to hit or stand?\n').lower()

        if choice[0] == 'h':
            playerDeck.append(r.randint(0,12))
            pscore += playerDeck[-1]
            if checker(pscore):
                print(f'The game is over. You exceeded 21 and lost! Your score was {pscore}')
                hit = False
                break
            else:
                print(f'{pscore} is your score.')
        if choice[0] == 's':
            hit = False
            break
    
    
    if checker(pscore):
        print('Your score was more than 21!')
    else:
        if pscore > dscore:
            print(f'You won! Your score was {pscore}, and the dealer had {dscore}')
            hit = False
        elif pscore == dscore:
            print('You tied with the dealer!')
            hit = False
        else:
            print(f'You lost! The dealer had {dscore}')
            hit = False
            
    
        
intro()

