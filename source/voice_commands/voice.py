import asyncio
from logging import error
import discord
from ..boot import *
from discord.ext import commands

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

