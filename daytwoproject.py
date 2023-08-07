print('Welcome to the Tip Calculator.\nHow much was the total bill?')
bill = float(input())
print('What percent are you tipping? 10, 12, 15')
tip = float(input())

print('How many people are paying for the bill?')
people = float(input())

splitBill = bill / people

tipPercent = tip / 100 + 1

tipBill = splitBill * tipPercent
finalBill = "{:.2f}".format(tipBill)
print(f'{finalBill} is how much the each person must pay in total.')
