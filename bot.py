import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import Pymoe
import datetime
import base64
import os
import random
import apiai
import gspread
import requests
import simplejson as json
import github
import json
import aiohttp
from io import BytesIO
from PIL import Image
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

def __init__(self, bot):
    self.session = aiohttp.ClientSession(loop=bot.loop)

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
async def update(ctx, message, content):
    g = github.Github(token)
    user = g.get_user()
    repo = user.get_repo('bot-test-discord-bot')
    #for repoo in g.get_user().get_repos():
    print(repo.name)
    file = repo.get_contents('/update.json')
    print(file.name)
    #repo.create_file('manimi/bot-test-discord-bot', 'Update', 'Good shit')
    repo.update_file('/update.json', message, content, file.sha)
    await bot.say("update.json has been updated!")
    
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
    filename = input("update.json")
    if (file):
        fp = open(filename)
        users = json.load(fp)

        time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user_id]['xp_time']
        if time_diff >= 120:
            users = {}
            users[user_id] = {user_id: {}}
            users[user_id]['xp'] += xp
            users[user_id]['xp_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
            json.dump(users, fp, sort_keys=True, indent=4)
            
@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*2, commands.BucketType.user)
async def cooldown(ctx):
    await bot.say("Check the cooldown now!")
          
@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*2, commands.BucketType.user)
async def cooldownhours(ctx):
    await bot.say("Check the cooldown now!")
    
@bot.command(pass_context=True)
@commands.cooldown(1, 60*60, commands.BucketType.user)
async def cooldownminutes(ctx):
    await bot.say("Check the cooldown now!")
    
@bot.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def cooldownseconds(ctx):
    await bot.say("Check the cooldown now!")
    
@bot.command(pass_context=True)
async def srb2image(ctx, url):
    theurl = 'https://www.srb2.org/wp-content/uploads/{}.png'.format(url)
    urlname = '{}.png'.format(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(theurl) as resp:
            buffer = BytesIO(await resp.read())

    await bot.send_file(ctx.message.channel, fp=buffer, filename=urlname)
    
@bot.command(pass_context=True)
async def scramble(ctx):
    async with session.post("http://watchout4snakes.com/wo4snakes/Random/RandomWord") as post:
        assert isinstance(post, aiohttp.ClientResponse)
        word = await post.read()
    word = word.decode()
    scrambled = random.sample(word, len(word))
    scrambled = ''.join(scrambled)
    await bot.say("The word scramble is: `{scrambled}`! You have 30 seconds to solve...")

    def check(m):
        return m.content == word and m.channel == ctx.message.channel

    try:
        msg = await bot.wait_for_message(timeout=30, content="message", check=check)
        if msg:
            await bot.say("Nice job! {msg.author.name} solved the scramble! The word was `{word}`!")
    except asyncio.TimeoutError:
        await bot.say("Oops! Nobody solved it. The word was `{word}`!")
        
@bot.command(pass_context=True)
async def longcat(ctx, match):
    body_length = min(len(match.group(1)), 20)
    width = cat_tail.width + body_length * cat_body.width + cat_head.width
    im = Image.new('RGBA', (width, cat_head.height), 0x00000000)
	
    im.paste(cat_tail, (0, 0))
    x = cat_tail.width
    for i in range(body_length):
	    im.paste(cat_body, (x, 0))
	    x += cat_body.width
    im.paste(cat_head, (x, 0))
	
    buf = io.BytesIO()
    im.save(buf, 'png')
    buf.seek(0)
    await bot.send_file(ctx.message.channel, fp=discord.File(buf, match.group(0) + '.png'))
    
@bot.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.CommandOnCooldown):
        hours = str(error.retry_after/3600)
        minutes = str(error.retry_after/60)
        secondss = str(error.retry_after)
        if (ctx.message.content == 'dd!cooldown'):
            await bot.send_message(channel, "This command is on cooldown. Try again in {}".format(datetime.timedelta(seconds=int(error.retry_after))))
        else:
            if (error.retry_after >= 3600):
                await bot.send_message(channel, "This command is on cooldown. Try again in {} hours.".format(hours[0:2]))
            elif ((error.retry_after >= 60)&(error.retry_after < 3600)):
                await bot.send_message(channel, "This command is on cooldown. Try again in {} minutes.".format(minutes[0:2]))
            elif (error.retry_after < 60):
                await bot.send_message(channel, "This command is on cooldown. Try again in {} seconds.".format(secondss[0:2]))
            
bot.run(bot_token)
