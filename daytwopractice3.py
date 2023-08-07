print('What is your age?')
age = int(input())

yearsR = 90 - age
weeksR = yearsR * 52
daysR = yearsR * 365
monthsR = yearsR * 12

print(f'You have {daysR} days, {monthsR} months, and {weeksR} weeks remaining until 90 years old.')