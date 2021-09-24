import discord
from ..boot import *
from discord.ext import commands
import requests

@sage.command()
async def joke(ctx):
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
    'x-rapidapi-key': "a7202c6505mshac4812d4e1434b3p1e7c3bjsn26341f464af9"
    }

    response = requests.request("GET", url, headers=headers)
    await ctx.reply(response.text)

@joke.error
async def joke(ctx, error):
    message = error
    await ctx.reply(message)