import discord
from ..boot import *
from discord.ext import commands

@sage.command()
@commands.has_any_role(830439735050371103,859475468343574558,859475468343574558,830486598050119740)
async def reply(ctx, link: discord.Message,*, message=''):
  if(message!=''):
     await link.reply(message)
     channel= discord.utils.get(sage.get_all_channels(), id=884027453100670986)
     embed= discord.Embed(title=f"{ctx.author}'s reply", description=f"**{ctx.author}** replied to **{link.author}**'s message on {ctx.author.guild}: {link.jump_url} \n \n **{link.author}'s message:** \t {link.content} \n \n **{ctx.author}'s reply:**\t {message}", color=0xff0000)
     embed.set_thumbnail(url=ctx.author.avatar_url)
     await channel.send(embed=embed)
     await ctx.message.add_reaction('👍')
  else:
      ctx.reply('``Error: Enter a message to be sent.``')

@reply.error
async def reply(ctx, error):
    message = error
    await ctx.reply(message)
