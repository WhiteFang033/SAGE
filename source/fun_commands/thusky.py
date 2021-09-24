import discord
from ..boot import *
from discord.ext import commands

#thusky_emoji
@sage.listen("on_message")
async def on_message(message):
    if ":thusky:" in message.content and message.author.id == 799186130654199809:
        await message.add_reaction("<:thusky:833256143975481344>")