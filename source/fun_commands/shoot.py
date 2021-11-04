import discord
from ..boot import *
from discord.ext import commands
from discord_components import *

@sage.command()
async def shoot(ctx, member: discord.Member):
    await ctx.send('Hands Up!'+member.mention)
    msg= await ctx.send(file=discord.File('././assets/pictures/gun op.jpg'),components= [[Button(style= ButtonStyle.green, label="Shoot"),
                                                                                             Button(style= ButtonStyle.blue, label="Blast!!!")]])
    def check(resp):
     return resp.user==ctx.author and resp.channel==ctx.channel
    resp= await sage.wait_for('button_click', check=check)
    
    if resp.component.label == "Shoot":
       await ctx.send(f"{member.mention} has been shot dead!")
       await ctx.send("https://tenor.com/view/get-rekt-boi-elmo-shot-execution-gif-15314352")
    elif resp.component.label == "Blast!!!":
        await ctx.send(f"BLASTING... \n2 minutes silence for {member.mention}! RIP.")
        await ctx.send("https://tenor.com/view/russia-soviet-missile-missile-truck-rocket-truck-gif-18785324")

@shoot.error
async def shoot(ctx, error):
    message = error
    await ctx.reply(message)