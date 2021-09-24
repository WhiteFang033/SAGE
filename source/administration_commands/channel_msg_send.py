import discord
from ..boot import *
from discord.ext import commands

@sage.command()
@commands.has_any_role(830439735050371103,859475468343574558,859475468343574558,830486598050119740)
async def csend(ctx, channel: discord.TextChannel,*,message=''):
    if(message!=''):
      await channel.send(message)
      await ctx.message.add_reaction('👍')
    else:
      await ctx.send('``Error: Enter a message to be sent.``')   

@csend.error
async def csend(ctx, error):
    message = error
    await ctx.reply(message)