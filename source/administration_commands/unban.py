import discord
from ..boot import *
from discord.ext import commands

@sage.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, member: discord.Member,*,reason='No reason specified.'):
    await member.unban(reason= reason)
    await ctx.send(member.name+'has been unbanned.')

@unban.error
async def unban(ctx, error):
    message = error
    await ctx.reply(message)