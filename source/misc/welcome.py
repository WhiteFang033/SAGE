from unicodedata import name
import discord
from ..boot import *
from discord.ext import commands

#welcome
@sage.listen("on_member_join")
async def on_member_join(member):
     channel = sage.get_channel(883664978509430825)
     await channel.send(f"{member.mention} \n **Welcome to the server {member.guild}. We are happy to have you here!**")
     verified = discord.utils.get(member.guild.roles, name="Verified")
     await member.add_roles(verified)