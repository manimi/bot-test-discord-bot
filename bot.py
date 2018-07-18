import discord
from discord.ext import commands
import Pymoe
import datetime
import os
import random
import apiai
import gspread
import requests as rq
import simplejson as json
import github
import json
from oauth2client.service_account import ServiceAccountCredentials

#GETTING API KEYS FROM HEROKU
#api = os.environ["RIOT_KEY"]
#wu_key = os.environ['WU_API']
#owm = os.environ['open_weather']
#img_api = os.environ['img_api']
#apiai_token = os.environ['api_ai']
bot_token = os.environ['BOT_TOKEN']
token = os.environ['TOKEN']
An = Pymoe.Anilist()

bot = commands.Bot(command_prefix='dd!')

epoch = datetime.datetime.utcfromtimestamp(0)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command(pass_context=True)
async def logout(ctx):
    """RESTARTS THE BOT IN HEROKU SERVER, BUT ENDS IN TERMINAL"""
    creator_id = 224185471826132992
    sender_id = ctx.message.author.id
    send_id = int(sender_id)
    if send_id == creator_id:
        await bot.say("Logging out bot now!")
        await bot.logout()
    else:
        await bot.say("Can not restart bot because you are not the creator")
        
@bot.command(pass_context=True)
async def check(ctx):
    g = github.Github()
    repo = g.get_repo('manimi/bot-test-discord-bot')
    #for repoo in g.get_user().get_repos():
    print(repo.name)
    file = repo.get_contents('/update.txt')
    print(file.name)
    #repo.create_file('manimi/bot-test-discord-bot', 'Update', 'Good shit')
    
@bot.command(pass_context=True)
async def update(ctx):
    g = github.Github(token)
    user = g.get_user()
    repo = user.get_repo('bot-test-discord-bot')
    #for repoo in g.get_user().get_repos():
    print(repo.name)
    file = repo.get_contents('/update.json')
    print(file.name)
    #repo.create_file('manimi/bot-test-discord-bot', 'Update', 'Good shit')
    repo.update_file('/update.json', 'Some Update', 'Message has been updated.', file.sha)
    await bot.say("Message has been updated!")
    
@bot.command(pass_context=True)
async def attempt(ctx):
    g = github.Github(token)
    user = g.get_user()
    repo = user.get_repo('bot-test-discord-bot')
    #for repoo in g.get_user().get_repos():
    print(repo.name)
    file = repo.get_contents('/update.json')
    print(file.name)
    #repo.create_file('manimi/bot-test-discord-bot', 'Update', 'Good shit')
    await bot.say("You tried!")
    if (file):
        with open('update.json', 'r') as fp:
            users = json.load(fp)

        time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['xp_time']
        if time_diff >= 120:
            users = {}
            users[user_id] = {user_id: {}}
            users[user_id]['xp'] += xp
            users[user_id]['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            g.dump(users, fp, protocol=0)
            
bot.run(bot_token)
