from ..boot import *

@sage.command(aliases=['fr'])
async def send_fr(ctx, member: discord.Member):

    await member.send_friend_request()
