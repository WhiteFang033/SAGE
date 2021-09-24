import discord
from ..boot import *
from discord.ext import commands

@sage.command()
@commands.has_any_role(830439735050371103,859475468343574558,830486598050119740)
async def cmds(ctx):
    embed= discord.Embed(title='Moderation Commands', description= 'Yo! We meet again,\n Here are my moderation commands, use them wisely: \n \n \n 1. !cmds \t - shows this message. \n \n  \n 2. !clear <number of messages to be deleted> or \n !cl <number of messages to be deleted> \t - to clear a number of messages. \n \n  \n 3. !dm <mention user> <message> \t - to direct message a user. \n \n   \n 4. !kick <mention user> <reason> \t - to kick a user. \n \n  \n 5. !ban <mention user> <reason> \t - to ban a member. \n \n  \n 6. !unban <mention user> <reason> \t - to unban a member. \n \n  \n 7. !msg <message> \t - to message in general channel. \n \n  \n 8. !csend <channel ID or channel name(with emoji)> <message> \t - to send a message to a specific channel.' , color=0xff0000)
    file=discord.File('sage.jpg')
    embed.set_image(url="https://static.wikia.nocookie.net/bleachfanfiction/images/e/e8/Hitorigami.jpg/revision/latest?cb=20180505120623")
    await ctx.send( embed=embed)

@cmds.error
async def cmds(ctx, error):
    message = error
    await ctx.reply(message)