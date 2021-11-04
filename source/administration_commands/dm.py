import discord
from ..boot import *
from discord.ext import commands
from discord import role

@sage.command()
@commands.has_any_role(830486598050119740,859475468343574558,830439735050371103,836122037009121312)
async def dm(ctx, member: discord.Member,*,Message=''):
     if(Message!=''):
      await member.send(Message)
      await ctx.message.add_reaction('👍')
     else:
      await ctx.send('``Error: Enter a Message.``')   

@dm.error
async def dm(ctx, error):
     message=error
     await ctx.reply(message)
