print('Welcome to the Leap Year Checker. Please type a year.')

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'The year {year} is a leap year.')
        else:
            print(f'The year {year} is not a leap year.')
    else:
        print(f'The year {year} is a leap year.')
else:
    print(f'The year {year} is not a leap year.')

    