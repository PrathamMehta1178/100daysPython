bill = 0
print('Welcome to Python Pizza!')
size = input('What size pizza do you want? S, M, or L\n')
if size.lower() == 's':
    bill += 15
elif size.lower() == 'm':
    bill += 20
else:
    bill += 25

p = input('Would you like extra pepperoni? Y or N\n')

if p.lower() == 'y' and size == 's':
    bill += 2

elif p.lower() == 'y':
    bill += 3
else:
    pass

c = input('Would you like any extra cheese with your pizza? Y or N\n')

if c.lower() == 'y':
    bill += 1
else:
    pass

print(f'Your total is ${bill}.')