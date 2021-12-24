from logging import error
from ..boot import *

@sage.command()
@commands.has_any_role(830486598050119740,859475468343574558,830439735050371103,836122037009121312)
async def medit(ctx, message: discord.Message,*,text):
    await message.edit(content=text)
    await ctx.message.add_reaction('👍')

@medit.error
async def edit(ctx, error):

    await ctx.reply(error)