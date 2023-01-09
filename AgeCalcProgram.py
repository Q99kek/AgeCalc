from datetime import datetime
current_time = datetime.now()

print('Welcome to the Age Calculator!\nPlease enter the following information to have your age precisely calculated:\n')

while True:
    try:
        year = int(input('What is your birth year?\n'))
        if year < current_time.year and year >= current_time.year - 100:
            break

        else:
            print('Error: You must enter a valid year.\n')
            continue

    except ValueError:
        print('Error: You must enter a whole number.\nFor example: 1996\n')
        continue

monthConversions = {'january': 1,'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

while True:
    in_str = input('What is your birth month?\n')
    in_str = monthConversions.get(in_str.lower(), in_str)

    try:
        month = int(in_str)

        if month > 12 or month < 1:
            raise ValueError
        break

    except ValueError:
        print('Error: You must enter the full name of the month or a whole number from 1 to 12.\n')

while True:
    try:
        day = int(input('What is your birth day?\n'))
        if month in [1, 3, 5, 7, 8, 10, 12] and day < 32 and day > 0:
            break

        elif month in [4, 6, 9, 11] and day < 31 and day > 0:
            break

        elif year % 400 == 0  and month == 2 and day < 30 and day > 0:
            break

        elif year % 4 == 0 and month == 2 and day < 30 and day > 0:
            break

        elif month == 2 and day <29 and day >0:
            break

        else:
            print('Error: You must enter a valid day.')
            continue

    except ValueError:
        print('Error: You must enter a whole number.\nFor example: 25')
        continue

print('\nYour birth date is ' + str(day) + '.' + str(month) + '.' + str(year) + '.')

ageyear = current_time.year - int(year)

if int(month) < current_time.month:
    ageyear = current_time.year - int(year)

elif int(month) >= current_time.month:
    ageyear = current_time.year - int(year) - 1

agemonth = current_time.month - int(month) + 12

if int(month) < current_time.month:
    agemonth = current_time.month - int(month) + 12

elif int(month) > current_time.month:
    agemonth = current_time.month - int(month) + 11

ageday = current_time.day - int(day) + 31

if int(day) == 31:
    ageday = current_time.day - int(day) + 31

elif int(day) <= 30:
    ageday = current_time.day - int(day) + 30

if int(month) == current_time.month and int(day) == current_time.day:
    agemonth = 0
    ageday = 0
    ageyear = current_time.year - int(year)

elif int(month) == current_time.month and ageday < 30:
    agemonth = current_time.month - int(month) + 11

elif int(month) == current_time.month and ageday > 30:
    agemonth = 0
    ageday = current_time.day - int(day)
    ageyear = current_time.year - int(year)

print('You are ' + str(ageyear) + ' years, ' + str(agemonth) + ' months, ' + 'and ' + str(ageday) + ' days old.')