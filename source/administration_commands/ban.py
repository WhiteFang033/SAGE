import discord
from ..boot import *
from discord.ext import commands

@sage.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member,*,reason='No reason specified.'):
    await member.send("You have been unbanned from the server \n Reason: "+reason)
    await ctx.send(member.name+'has been banned.')
    await member.ban(reason= reason)
    
@ban.error
async def ban(ctx, error):
    message = error
    await ctx.reply(message)