import random
import discord
from discord.ext import commands
from bot_logic import gen_pass
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
@bot.command()
async def hello(message):
      await message.send("Hi!")
@bot.command()
async def bye(message):
      await message.send("\\U0001f642")     
@bot.command()
async def пароль(message):
      await message.send(gen_pass(10))       
@bot.command()
async def монетка(message):
      await message.send(coin()) 
bot.run("MTEwNDY3MzI1MDU4OTU0MDQ2Mg.GSByYx.fVjjIvlP-wjwhckevFNqkwFk1rvH8NfOavNv2s")