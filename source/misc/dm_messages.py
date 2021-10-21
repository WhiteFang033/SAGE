import discord
from ..boot import *
from discord.utils import *
from discord.ext import commands


#DM messages
@sage.listen("on_message")
async def on_message(message):
    if message.guild is None and message.author != sage.user:
         channel= discord.utils.get(sage.get_all_channels(), id=883651133749493781)
         pfp= message.author.avatar_url
         embed= discord.Embed(title=f"{message.author}'s Message",description=f"{message.content}",color=0xff0000)
         embed.set_thumbnail(url=pfp)
         await channel.send(message.author.mention, embed=embed)
         await message.add_reaction('👍')
    else:
        return