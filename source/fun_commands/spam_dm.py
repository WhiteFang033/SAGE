import discord
from ..boot import *

@sage.command()
@commands.has_any_role(830486598050119740, 859475468343574558, 830439735050371103)
async def spam(ctx, x:int, member:discord.Member,*, message):

    for x in range(x):
        await member.send(message)

@spam.error
async def spam(ctx, error):
    message = error
    await ctx.reply(message)