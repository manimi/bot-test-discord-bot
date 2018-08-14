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
from PIL import Image, ImageDraw, ImageOps
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup

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
async def srb2(ctx, option=None):
    if (option is None):
        await bot.say("Use dd!srb2 status")
    elif ((option == "status")|(option == "STATUS")|(option == "Status")):
        r = requests.get('https://srb2.org')
        json_data = json.loads(r.text)
        status_server = json_data['status']
        await bot.say('{}'.format(json_data))
    else:
        await bot.say("Not available option!")
        
@bot.command(pass_context=True)
async def test(ctx):
    link = "https://www.architecture.com/FindAnArchitect/FAAPractices.aspx?display=50"

    html = requests.get(link).text

    soup = BeautifulSoup(html, "lxml")
    res = soup.findAll("article", {"class": "listingItem"})
    for r in res:
        print("Company Name: " + r.find('a').text)
        print("Address: " + r.find("div", {'class': 'address'}).text)
        print("Website: " + r.find_all("div", {'class': 'pageMeta-item'})[3].text)

@bot.command(pass_context=True)
async def image(ctx):
    width = random.randint(1, 500)
    height = random.randint(1,500)
    red = random.randint(1, 255)
    blue = random.randint(1, 255)
    green = random.randint(1, 255)

    size = str(width) + ", " + str(height)
    colour = str(red) + ", " + str(green) + ", " + str(blue)

    img = Image.new('RGB', (width, height), (red, green, blue))
    img.save("pic.png", "PNG")
    await bot.send_file(ctx.message.channel, "pic.png")
    
@bot.command(pass_context=True)
async def shrug(ctx):
    user = ctx.message.author
    img1 = Image.open(fp=open("shrug.png", "rb"))
    async with aiohttp.ClientSession() as session:
        async with session.get(user.avatar_url) as avatar:
            data = await avatar.read()
            av_bytes = BytesIO(data)
            avatar = Image.open(av_bytes)
    dest = (155, 70)
    size = avatar.size
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    av = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    av.putalpha(mask)

    face_1 = av.resize((78, 78), Image.LANCZOS)
    face_1 = face_1.rotate(15, expand=True)

    img1.paste(face_1, dest, face_1)

    dest = (351, 43)
    size = avatar.size
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    av = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    av.putalpha(mask)

    face_2 = av.resize((36, 36), Image.LANCZOS)
    face_2 = face_2.rotate(-4, expand=True)

    img1.paste(face_2, dest, face_2)

    dest = (350, 225)
    size = avatar.size
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    av = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    av.putalpha(mask)

    face_3 = av.resize((40, 40), Image.LANCZOS)
    face_3 = face_3.rotate(5, expand=True)

    img1.paste(face_3, dest, face_3)
    
    img1.save("shrg.png", "PNG")
    await bot.send_file(ctx.message.channel, "shrg.png")
    
@bot.command(pass_context=True)
async def gem(ctx):
    red = random.randint(1, 255)
    blue = random.randint(1, 255)
    green = random.randint(1, 255)
    user = ctx.message.author
    gem = Image.open(fp=open("gem.png", "rb"))
    gemm = Image.open("gemm.png")
    print("opened alt gem")
    background = Image.new('RGB', (gem.width, gem.height), (red, green, blue))
    async with aiohttp.ClientSession() as session:
        async with session.get(user.avatar_url) as avatar:
            data = await avatar.read()
            av_bytes = BytesIO(data)
            avatarr = Image.open(av_bytes)
    dest = (5, 5)
    size = avatarr.size
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    av = ImageOps.fit(avatarr, mask.size, centering=(0.5, 0.5))
    av.putalpha(mask)
    
    destt = (45, 92)
    sizee = gem.size
    maskk = Image.new('L', sizee, 0)
    draww = ImageDraw.Draw(maskk)
    draww.ellipse((0, 0) + sizee, fill=255)
    avv = ImageOps.fit(gem, maskk.size, centering=(0.5, 0.5))
    avv.putalpha(maskk)

    face_1 = avv.resize((30, 30), Image.LANCZOS)
    #face_1 = face_1.rotate(15, expand=True)
    
    backgroundd = Image.new("RGBA", avatarr.size)
    
    print("alt bg")
    
    backgroundd.paste(avatarr, (0,0))
    
    print("paste av")
    
    backgroundd.paste(gemm, (0,0), gemm)
    
    print("paste alt gem")
    
    #Image.alpha_composite(background, gem).save('gempic.png')
    
    backgroundd.save("gempic.png", "PNG")
    
    print("save alt bg")
    
    await bot.send_file(ctx.message.channel, "gempic.png")
    
    print("k.")

@bot.command(pass_context=True)
async def profile(ctx):
    await bot.send_typing(ctx.message.channel)

    eTitle = 'Profile'
    eDesc = ''

    em = discord.Embed(title=eTitle,url=ctx.message.author.avatar_url.replace('webp','png'),description=eDesc,colour=discord.Colour.orange())
    em.set_author(name="{}".format(ctx.message.author.name), url=ctx.message.author.avatar_url.replace('webp','png'), icon_url=ctx.message.author.avatar_url.replace('webp','png'))
    em.add_field(name="XP :sparkles:", value='1', inline=True)
    em.add_field(name="Level :star2:", value='2', inline=True)
    em.add_field(name="Credits :moneybag:", value='3', inline=True)
    em.add_field(name="Inventory :shopping_bags:", value='- h -', inline=True)
    em.add_field(name="Holds :handbag:", value='g', inline=True)
    em.set_thumbnail(url=ctx.message.author.avatar_url.replace('webp','png'))
    em.set_footer(text='Requested by: {}'.format(ctx.message.author.name))
    sn = await bot.say(embed=em)
    
    if (len(sn.embeds) == 1):
        print(sn.embeds[0]['title'])
        
@bot.command(pass_context=True)
async def playfile(ctx, file):
    for server in bot.servers:
        if (ctx.message.author.id == '224185471826132992'):
            voice = bot.voice_client_in(server)
            player = voice.create_ffmpeg_player(file)
            player.start()
            return None

@bot.command(pass_context=True)
async def connect(ctx, id):
    if (ctx.message.author.id == '224185471826132992'):
        channel = bot.get_channel(id)
        await bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def disconnect(ctx, id):
    if (ctx.message.author.id == '224185471826132992'):
        server = bot.get_server(id)
        voice = bot.voice_client_in(server)
        await voice.disconnect()
        
@bot.command(pass_context=True)
async def find(ctx, con : str):
    counter = []
    #print("counter installed")
    async for message in bot.logs_from(ctx.message.channel):
        if ((con in message.content)&(message != ctx.message)):
            #print(message.author.name)
            counter.append( [message.author.name,message.content,str(message.timestamp),message.author.avatar_url] )
    #print("done searching")
    c = random.choice(counter)
    #print("pick a random item that fits")
    #msg = bot.get_message(ctx.message.channel, c)
    #print("get the message from id")
    #await bot.say(c[1])
    #await bot.say(c[0])
   
    eTitle = c[1]
    eDesc = c[2]

    em = discord.Embed(title=eTitle,description=eDesc,colour=discord.Colour.orange())
    em.set_author(name="{}".format(c[0]), url=c[3].replace('webp','png'), icon_url=c[3].replace('webp','png'))
    em.set_footer(text='Requested by: {}'.format(ctx.message.author.name))
    await bot.send_message(ctx.message.channel,embed=em)
    
@bot.command(pass_context=True)
async def ultimate(ctx, url : str=None, text : str=None):
    if ((url is None)|(text is None)):
        await bot.say("Please type an url of an image and the additional text.")
    else:
        urlname = 'ultimateleak.png'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                buffer = BytesIO(await resp.read())

        await bot.send_file(ctx.message.channel, fp=buffer, filename=urlname, content=text)

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
