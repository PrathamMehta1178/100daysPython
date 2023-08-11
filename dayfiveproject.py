import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letterPW = []
numbersPW = []
symbolsPW = []
password = ''
print("Welcome to the PyPassword Generator!")

# collect data 

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# choose randomized things 

for i in range(nr_letters):
    selectL = r.randint(0, 51) # selecting a letter
    letterPW.append(letters[selectL])

for i in range(nr_symbols):
    selectS = r.randint(0, 8) # selecting a letter
    symbolsPW.append(symbols[selectS])

for i in range(nr_numbers):
    selectN = r.randint(0, 9) # selecting a letter
    numbersPW.append(numbers[selectN])



# randomly print out the list

while len(letterPW) + len(symbolsPW) + len(numbersPW) != 0:
    listChooser = r.randint(0,2)

    if listChooser == 0 and letterPW:
        pletter = r.choice(letterPW)
        letterPW.remove(pletter)
        password = password + pletter
    
    if listChooser == 1 and symbolsPW:
        psymbol = r.choice(symbolsPW)
        symbolsPW.remove(psymbol)
        password = password + psymbol
    
    if listChooser == 2 and numbersPW:
        pnumber = r.choice(numbersPW)
        numbersPW.remove(pnumber)
        password = password + pnumber
    else:
        pass
    
print(f'{password} is your password.')