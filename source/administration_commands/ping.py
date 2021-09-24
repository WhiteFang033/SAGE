import discord
from ..boot import *
from discord.ext import commands

@sage.command()
async def ping(ctx):
    await ctx.reply("pong!")