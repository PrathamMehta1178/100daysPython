print('Welcome to the Love Calculator!')
fname = input('Please type the first name\n')
sname = input('Please type the second name\n')

cname = fname + sname

firstNum = cname.count('t')
firstNum += cname.count('r')
firstNum += cname.count('u')
firstNum += cname.count('e')

secNum = cname.count('l')
secNum += cname.count('o')
secNum += cname.count('v')
secNum += cname.count('e')

final = str(firstNum) + str(secNum)

if int(final) < 10 or int(final) > 90:
    print(f'The score is {final} and you go together like Coke and Mentos')
elif int(final) >= 40 and int(final) <= 50:
    print(f'Your score is {final} and you\'re alright.')
else:
    print(f'Your score is {final}.')