import asyncio
from logging import error
import discord
from ..boot import *
from .yt_play import  *
from discord.ext import commands
import json 
import requests

@sage.command(aliases=['c'])
async def connect(ctx):
    voice_channel = ctx.author.voice
    await voice_channel.channel.connect()
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild) 
    await asyncio.sleep(2)
    voice.play(discord.FFmpegPCMAudio('media/mp3/alpha/connected.mp3'))
    await asyncio.sleep(2)
    voice.play(discord.FFmpegPCMAudio('media/mp3/alpha/hello.mp3'))

    
@sage.command()
async def leave(ctx):
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    await voice.disconnect()

@connect.error
async def connect(ctx, error):
    message= error
    await ctx.reply(message)
@leave.error
async def leave(ctx, error):
    message= error
    await ctx.reply(message)

@sage.command(aliases=['pse'])
async def pause(ctx):
    voice= discord.utils.get(sage.voice_clients, guild= ctx.guild)
    voice.pause()

@pause.error
async def pause(ctx, error):
  message = error
  await ctx.reply(message)

@sage.command(aliases=['r'])
async def resume(ctx):
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    voice.resume()
@resume.error
async def resume(ctx,error):
    message= error
    await ctx.reply(message)

@sage.command(aliases=['s'])
async def stop(ctx):
    voice = discord.utils.get(sage.voice_clients, guild= ctx.guild)
    voice.stop()
@stop.error
async def stop(ctx,error):
    message = error
    await ctx.reply(message)

@sage.command()
async def lyrics(ctx,*,song):

 if song =="":
    for title in search_music:
            song = title
        
    if song == "":
            await ctx.reply("``Enter the title of the song.``")
            return
    return

        

 url = "https://shazam.p.rapidapi.com/auto-complete"

 querystring = {"term":f"{song}","locale":"en-US"}

 headers = {
    'x-rapidapi-host': "shazam.p.rapidapi.com",
    'x-rapidapi-key': "a7202c6505mshac4812d4e1434b3p1e7c3bjsn26341f464af9"
    }

 response = requests.get(url, headers=headers, params=querystring)

 await ctx.reply(response.text)

 print(response.text)

