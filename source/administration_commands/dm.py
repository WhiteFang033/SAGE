import discord
from ..boot import *
from discord.ext import commands
from discord import role

@sage.command()
@commands.has_permissions(manage_roles = True)
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
