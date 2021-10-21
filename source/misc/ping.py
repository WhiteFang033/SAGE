import discord
from ..boot import *
from discord.ext import commands


@sage.listen("on_message")
async def on_message(message):
     if message.content == "ping":
      await message.reply("pong!")


