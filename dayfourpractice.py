import random as r
combined_names = input('Welcome to Banker Roulette\nPlease type everyone\'s name seperated by a comma.\n')
names = combined_names.split(', ')
max  = len(names)
chooser = r.randint(0,max)
chosen = names[chooser]
print(f'{chosen} is paying for the bill!')