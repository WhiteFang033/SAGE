import discord
from .boot import *
from discord.ext import commands


@sage.listen("on_message")
async def on_message(message):

    if 'i am back' in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')

    if 'I am back' in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')

    if "I'm back" in message.content:
       await message.reply(f'Welcome Back {message.author.name}!')