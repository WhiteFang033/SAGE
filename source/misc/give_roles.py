import discord
from ..boot import *
import discord.utils


@sage.command()
@commands.has_permissions(kick_members = True)
async def add_role(ctx, member:discord.Member, rolename):
    role= discord.utils.find(
           lambda r: r.name == rolename, ctx.message.guild.roles
          )
    await member.add_roles(role)

@add_role.error
async def add_role(ctx, error):
    message = error
    await ctx.reply(error)