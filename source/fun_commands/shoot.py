import discord
from ..boot import *
from discord.ext import commands

@sage.command()
async def shoot(ctx, member: discord.Member):
    await ctx.send('Hands Up!'+member.mention)
    msg= await ctx.send(file=discord.File('././assets/pictures/gun op.jpg'))
    
@shoot.error
async def shoot(ctx, error):
    message = error
    await ctx.reply(message)