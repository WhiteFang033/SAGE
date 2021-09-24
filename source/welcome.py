import discord
from .boot import *
from discord.ext import commands

#welcome
@sage.event
async def on_member_join(member):
    if member.guild == "『HiddenLeaf』":
     channel = member.guild.get_channel(883664978509430825)
     await channel.send(f"{member.mention} \n **Welcome to the server {member.guild}. We are happy to have you here!**")
     genin = sage.get(member.guild.roles, name="Genin")
     await member.add_roles(genin)