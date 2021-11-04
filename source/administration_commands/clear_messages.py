import discord
from ..boot import *
from discord.ext import commands

@sage.command(aliases=['cl'])
@commands.has_any_role(830486598050119740,859475468343574558,830439735050371103,836122037009121312)
async def clear(ctx, amount=0):
    await ctx.send('Messages Exocrised')
    
    await ctx.channel.purge(limit=(amount+2))