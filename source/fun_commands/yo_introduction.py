import discord
from ..boot import *
from discord.ext import commands
import typing
import asyncio


@sage.command()
async def yo(ctx):
 embed= discord.Embed(title='SAGE OF SIX PATHS', description= "Yo! I am The Sage of Six Paths, the Master Bot of The HiddenLeaf server. Feel free to use me.\n Here are list of commands that you can use to operate me! \n 1. !ping - pong! \n\n 2. !shoot <mention user> - to shoot a user. \n\n 3. !avatar <mention user> - to get a user's avatar \n\n 4. !w - to search on Wolfram|Alpha \n \n And Here are My Music Commands \n\n 1. !connect or !c - to connect to a voice channel \n\n 2. !leave - to disconnect \n\n3. !pause or !pse- to pause \n\n 4. !resume or !r- to resume \n\n 5. !stop or !s - to stop playing the current audio \n\n 6. !play - to play inbuild songs. \n\n 7. !p <title> - to play songs/audio from a youtube video", color=0xff0000)
 embed.set_image(url="https://static.wikia.nocookie.net/bleachfanfiction/images/e/e8/Hitorigami.jpg/revision/latest?cb=20180505120623")
 await ctx.send( embed=embed)

@sage.listen("on_message")
async def on_message(message):
  
  if message.content =="<@!872024188477669416>":
     async with message.channel.typing():
        await asyncio.sleep(1)
        await message.reply("At your service!")