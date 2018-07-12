import discord
from discord.ext import commands
import random

bot = discord.Client()
bot = commands.Bot(command_prefix='dd!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(bot_token)
