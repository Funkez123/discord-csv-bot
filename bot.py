import os
import numpy as np
from numpy import loadtxt
import discord
from discord.ext import commands
import random
import os

my_data = np.genfromtxt('new.csv', delimiter=';', dtype=None, encoding='utf-8')

prefix = "?"
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)
@bot.event
async def on_ready():
    print("Bot ist am laufen~")


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''
    latency = bot.latency  
    await ctx.send(latency)

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command()
async def anime(ctx):
    '''
    will recommend you an anime/anime-movie
    '''
#
    anime_db_value = my_data[random.randint(0,972)]
    rating = float(anime_db_value[3])/100
    rating_str = str(rating)
    recommendation = f'Have you seen {anime_db_value[0]}?' + '\n' + f'It has {anime_db_value[2]} Episode[s] and a rating of {rating_str} / 10 !' 
    await ctx.send(recommendation)


bot.run(os.environ["DISCORD_TOKEN"])
