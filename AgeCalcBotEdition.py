from datetime import datetime
import discord
from discord.ext import commands
import asyncio

current_time = datetime.now()

token = 'MTA2MTI5NDgzMzE2NTE2MDQ1OQ.Gi2jv2.0TZewU4EhOdf3Ulj6OTcR-T7JhTizH4fBbJgFg'
bot = commands.Bot(command_prefix='', intents=discord.Intents.all())
bot.Prefix = '!'


@bot.event
async def on_message(message):
    args = str(message.content).lower().split(' ')
    if args[0] == bot.Prefix + 'age':
        year = args[1]
        month = args[2]
        day = args[3]
        value_error = False
        month_error = False
        year_error = False

    while year_error == False:
        try:
            year = args[1]
            if int(year) < current_time.year and int(year) >= current_time.year - 100:
                break
            else:
                year_error = True
                value_error = True
                await message.channel.send('Error: You must enter a valid year in the form of a whole number.\nFor example: 1996\n')
                break
        except ValueError:
            year_error = True
            await message.channel.send('Error: You must enter a valid year in the form of a whole number.\nFor example: 1996\nPlease correct your input and try again.')
            break


    monthConversions = {'january': 1,'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

    global in_str
    in_str = ''

    while True:
        try:
            in_str = args[2]
            in_str = monthConversions.get(in_str.lower(), in_str)
            month = int(in_str)
            if 0 < month < 13:
                break
            else:
                month_error = True
                value_error = True
                await message.channel.send('Error: You must enter the full name of the month or a whole number from 1 to 12.\n')
                break
        except ValueError:
            month_error = True
            value_error = True
            await message.channel.send('Error: You must enter the full name of the month or a whole number from 1 to 12.\nPlease correct your input and try again.')
            break


    while month_error == False and year_error == False:
        try:
            day = args[3]
            if int(month) in [1, 3, 5, 7, 8, 10, 12] and int(day) < 32 and int(day) > 0:
                break

            elif int(month) in [4, 6, 9, 11] and int(day) < 31 and int(day) > 0:
                break

            elif int(year) % 400 == 0  and int(month) == 2 and int(day) < 30 and int(day) > 0:
                break

            elif int(year) % 4 == 0 and int(month) == 2 and int(day) < 30 and int(day) > 0:
                break

            elif int(month) == 2 and int(day) <29 and int(day) >0:
                break

            else:
                value_error = True
                await message.channel.send('Error: You must enter a valid day in the form of a whole number.\nFor example: 25')
                break

        except ValueError:
            value_error = True
            await message.channel.send('Error: You must enter a valid day in the form of a whole number.\nFor example: 25\nPlease correct your input and try again.')
            break


    if year_error == False:
        ageyear = current_time.year - int(year)

    if int(month) < current_time.month and year_error == False:
        ageyear = current_time.year - int(year)

    elif int(month) >= current_time.month and year_error == False:
        ageyear = current_time.year - int(year) - 1
        agemonth = current_time.month - int(month) + 12

    if int(month) < current_time.month and year_error == False:
        agemonth = current_time.month - int(month) + 12

    elif int(month) > current_time.month and year_error == False:
        agemonth = current_time.month - int(month) + 11
        ageday = current_time.day - int(day) + 31

    if int(day) == 31 and year_error == False:
        ageday = current_time.day - int(day) + 31

    elif int(day) <= 30 and year_error == False:
        ageday = current_time.day - int(day) + 30

    if int(month) == current_time.month and int(day) == current_time.day and year_error == False:
        agemonth = 0
        ageday = 0
        ageyear = current_time.year - int(year)

    elif int(month) == current_time.month and ageday < 30 and year_error == False:
        agemonth = current_time.month - int(month) + 11

    elif int(month) == current_time.month and ageday > 30 and year_error == False:
        agemonth = 0
        ageday = current_time.day - int(day)
        ageyear = current_time.year - int(year)


    if value_error == False and year_error == False:
        await message.channel.send('\nYour birth date is ' + str(day) + '.' + str(month) + '.' + str(year) + '.')
        await message.channel.send('You are ' + str(ageyear) + ' years, ' + str(agemonth) + ' months, ' + 'and ' + str(ageday) + ' days old.')
    elif value_error == True:
        await message.channel.send('Please correct your input and try again.')

bot.run(token)