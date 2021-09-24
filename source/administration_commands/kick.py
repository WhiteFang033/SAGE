import discord
from ..boot import *
from discord.ext import commands

@sage.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member,*,reason='No reason specified.'):
    await member.send("You have been kicked out of the server \n Reason: "+reason)
    await ctx.send(member.name+'has been exocrised- \n I- I mean kicked.')
    await member.kick(reason= reason)

@kick.error
async def kick(ctx, error):
    message = error
    await ctx.reply(message)