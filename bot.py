import discord
from discord.ext import commands
import Pymoe
import os
import random
import apiai
import gspread
import requests as rq
import simplejson as json
import github
from oauth2client.service_account import ServiceAccountCredentials

#GETTING API KEYS FROM HEROKU
#api = os.environ["RIOT_KEY"]
#wu_key = os.environ['WU_API']
#owm = os.environ['open_weather']
#img_api = os.environ['img_api']
#apiai_token = os.environ['api_ai']
bot_token = os.environ['BOT_TOKEN']
An = Pymoe.Anilist()

bot = commands.Bot(command_prefix='dd!')

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
async def update(ctx):
    g = github.Github()
    repo = g.get_repo('manimi/bot-test-discord-bot')
    file = repo.get_file_contents("/update.json")
    repo.update_file("/update.json", "Commit Comments", content, sha)

bot.run(bot_token)
