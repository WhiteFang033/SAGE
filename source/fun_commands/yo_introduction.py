import discord
from ..boot import *
from discord.ext import commands


@sage.command()
async def yo(ctx):
 embed= discord.Embed(title='SAGE OF SIX PATHS', description= "Yo! I am The Sage of Six Paths, the Master Bot of The HiddenLeaf server. Feel free to use me.\n Here are list of commands that you can use to operate me! \n 1. !ping - pong! \n\n 2. !shoot <mention user> - to shoot a user. \n\n 3. !reply <message link> <message> - to make SAGE reply to a particular message.  \n\n 4. !dance - Dancin'\n\n 5. !avatar <mention user> - to get a user's avatar", color=0xff0000)
 embed.set_image(url="https://static.wikia.nocookie.net/bleachfanfiction/images/e/e8/Hitorigami.jpg/revision/latest?cb=20180505120623")
 await ctx.send( embed=embed)