
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
print('Welcome to Treasure Map Maker.')
print('Please type in a column/row format for where you want the x to be. ex 22 or 31')

spot = input()

x1 = int(spot[0]) - 1

x2 = int(spot[1]) - 1

map[x2][x1] = 'x'

print(f"{row1}\n{row2}\n{row3}")


