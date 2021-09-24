import discord
from ..boot import *
from discord.ext import commands

@sage.command()
async def avatar(ctx,*, member: discord.Member):
    pfp= member.avatar_url
    embed= discord.Embed(title=f"{member}'s avatar", colour=0xff0000)
    embed.set_image(url=pfp)
    await ctx.reply(embed=embed)

@avatar.error
async def avatar(ctx, error):
    message = error
    await ctx.reply(message)