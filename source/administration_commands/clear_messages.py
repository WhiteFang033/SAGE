import discord
from ..boot import *
from discord.ext import commands

@sage.command(aliases=['cl'])
@commands.has_permissions(manage_roles = True)
async def clear(ctx, amount=0):
    await ctx.send('Messages Exocrised')
    
    await ctx.channel.purge(limit=(amount+2))