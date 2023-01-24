from datetime import datetime
import discord
from discord.ext import commands
import asyncio

current_time = datetime.now()

token = ''
bot = commands.Bot(command_prefix='', intents=discord.Intents.all())
bot.Prefix = '!'

@bot.event
async def on_message(message):
    args = str(message.content).lower().split(' ')
    if args[0] == 'bruh':
        await message.channel.send(':moyai:')

    elif args[0].startswith(bot.Prefix):
        if args[0].startswith(bot.Prefix) and args[0][len(bot.Prefix):] == 'help' or args[0][len(bot.Prefix):] == 'h':
            embed = discord.Embed(title="**Welcome to AgeCalc!**",
                                  description = "Here is a list of all available commands:\n", color=discord.Color.from_rgb(148, 164, 180))
            embed.set_thumbnail(url="http://www.newdesignfile.com/postpic/2016/05/gear-and-wrench-icon_401002.png")
            embed.add_field(name="\n`!help` or `!h`",
                                value="Gives a list and a short description of all available commands.\n",
                                inline=False)
            embed.add_field(name="\n`!agecalc` or `!ac`",
                                value="Precisely calculates your age based on YYYY/MM/DD input.\n"
                                      "Example of use: ``!ac 2000 2 29`` / ``!agecalc 2000 february 29``",
                                inline=False)
            embed.add_field(name="\n`!date` or `!d`",
                            value="Shows the current date and time.\n",
                            inline=False)
            await message.channel.send(embed = embed)

        elif args[0].startswith(bot.Prefix) and args[0][len(bot.Prefix):] == 'date' or args[0][len(bot.Prefix):] == 'd':
            embed = discord.Embed(color=discord.Color.from_rgb(225, 74, 58))
            embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678120-calendar-clock-512.png")
            embed.add_field(name="\nCurrent date is:",
                            value= current_time.strftime('%y-%m-%d'),
                            inline=False)
            embed.add_field(name="\nCurrent time is:",
                            value= current_time.strftime('%H:%M:%S'),
                            inline=False)
            await message.channel.send(embed=embed)

        elif args[0].startswith(bot.Prefix) and (args[0][len(bot.Prefix):] == 'agecalc' or args[0][len(bot.Prefix):] == 'ac'):
            year = args[1]
            month = args[2]
            day = args[3]
            year_error = False
            value_error = False
            month_error = False

        while year_error == False:
            try:
                year = args[1]
                if int(year) < current_time.year and int(year) >= current_time.year - 100:
                    break
                else:
                    year_error = True
                    value_error = True
                    await message.channel.send('**Error:** This bot uses ``YYYY/MM/DD`` input system.\nYou must enter a valid year in the form of a whole number.')
                    break
            except ValueError:
                year_error = True
                await message.channel.send('**Error:** This bot uses ``YYYY/MM/DD`` input system.\nYou must enter a valid year in the form of a whole number.\n*Please correct your input and try again.*')
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
                    await message.channel.send('**Error:** You must enter the full name of the month or a whole number from 1 to 12.\n')
                    break
            except ValueError:
                month_error = True
                value_error = True
                await message.channel.send('**Error:** You must enter the full name of the month or a whole number from 1 to 12.\n*Please correct your input and try again.*')
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
                    await message.channel.send('**Error:** You must enter a valid day in the form of a whole number.')
                    break

            except ValueError:
                value_error = True
                await message.channel.send('**Error:** You must enter a valid day in the form of a whole number.\n*Please correct your input and try again.*')
                break

        if int(month) == current_time.month and int(day) == current_time.day and year_error == False:
            agemonth = current_time.month - int(month)
            ageday = current_time.day - int(day)
            ageyear = current_time.year - int(year)
            await message.channel.send('https://giphy.com/gifs/moodman-happy-birthday-cat-eRXQ9JRiOHSNwVoGxt')

        elif int(month) == current_time.month and int(day) > current_time.day and year_error == False:
            agemonth = current_time.month - int(month) + 12
            ageday = current_time.day - int(day) + 30
            ageyear = current_time.year - int(year) - 1

        elif int(month) == current_time.month and int(day) < current_time.day and year_error == False:
            agemonth = current_time.month - int(month)
            ageday = current_time.day - int(day)
            ageyear = current_time.year - int(year)

        elif int(month) > current_time.month and int(day) == current_time.day and year_error == False:
            agemonth = current_time.month + 12 - int(month)
            ageday = current_time.day - int(day)
            ageyear = current_time.year - int(year) - 1

        elif int(month) > current_time.month and int(day) > current_time.day and year_error == False:
            agemonth = current_time.month + 12 - int(month) - 1
            ageday = current_time.day - int(day) + 30
            ageyear = current_time.year - int(year) - 1

        elif int(month) > current_time.month and int(day) < current_time.day and year_error == False:
            agemonth = current_time.month + 12 - int(month)
            ageday = current_time.day - int(day)
            ageyear = current_time.year - int(year) - 1

        elif int(month) < current_time.month and int(day) == current_time.day and year_error == False:
            agemonth = current_time.month - int(month)
            ageday = current_time.day - int(day)
            ageyear = current_time.year - int(year)

        elif int(month) < current_time.month and int(day) > current_time.day and year_error == False:
            agemonth = current_time.month - int(month) + 12
            ageday = current_time.day - int(day) + 30
            ageyear = current_time.year - int(year) - 1

        elif int(month) < current_time.month and int(day) < current_time.day and year_error == False:
            agemonth = current_time.month - int(month)
            ageday = current_time.day - int(day)
            ageyear = current_time.year - int(year)

        if value_error == False and year_error == False:
            embed = discord.Embed(title = '**Your age has been successfully calculated!**', color = discord.Color.from_rgb(235, 219, 171))
            embed.set_thumbnail(url="https://images.vexels.com/media/users/3/143394/isolated/preview/bd28922a768d08852f3023ed90b37248-bolo-de-anivers-rio-plano-by-vexels.png")
            embed.add_field(name ='\nYour birth date is:',
                            value = str(day) + '.' + str(month) + '.' + str(year) + '.\n',
                            inline = True)
            embed.add_field(name='\nYou are:',
                            value= str(ageyear) + ' years, ' + str(agemonth) + ' months, ' + 'and ' + str(ageday) + ' days old.',
                            inline=False)
            await message.channel.send(embed = embed)
        elif value_error == True:
            await message.channel.send('*Please correct your input and try again.*')

bot.run(token)
