import discord
from ..boot import *
from discord.ext import commands
import typing
import asyncio

count = 0
@sage.listen("on_message")
async def on_message(message):

   if 'i am back' in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')

   if 'I am back' in message.content:
      if message.author.id == 827027306077749328 or message.author.id == 819439855880372246:
       global count 
       count+=1
       if count == 3:
           count = 0
           await message.reply("...")
           await asyncio.sleep(2)
           async with message.channel.typing():
              await message.channel.send("So what?")
              await asyncio.sleep(2)
              await message.reply("Everyone already know that you are here. -_-")
      else:
       await message.reply(f'Welcome Back {message.author.name}!')

   if "I'm back" in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')
   
   if "I m back" in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')
   if "Im back" in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')
   if "im back" in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')
   
   if "i'm back" in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')
   
   if "i m back" in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')
   
    