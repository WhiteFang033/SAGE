import asyncio
import discord
from ..boot import *
from discord.ext import commands
import requests
import json
import typing
import tokens

@sage.command()
async def joke(ctx):
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
    'x-rapidapi-key': tokens.rapid_api_key 
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    body = data["body"]

    if body[0]["NSFW"]== False:
      setup= body[0]["setup"]
      punchline= body[0]["punchline"]
      joke= await ctx.send(setup)
      await asyncio.sleep(5)
      await joke.reply(punchline)
    
    else:
        await ctx.invoke(sage.get_command('joke'))

    


@joke.error
async def joke(ctx, error):
    message = error
    await ctx.reply(message)
