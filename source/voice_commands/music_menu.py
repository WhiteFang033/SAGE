import discord
from ..boot import *
from .music import *
from discord.ext import commands

@sage.command()
async def play(ctx):
    msg= await ctx.send("**Choose a song**", 
                    components=[[Button(style= ButtonStyle.green ,label="Pirates of Caribbean"),
                                 Button(style= ButtonStyle.green ,label="Rinkiya ke Papa"),
                                 Button(style= ButtonStyle.green ,label="Jeena Jeena"),
                                 Button(style= ButtonStyle.green ,label="Chahun me ya na"),
                                 Button(style= ButtonStyle.green ,label="Last Day On Earth")
                                ],
                                
                                [
                                Button(style= ButtonStyle.green ,label="Lovely")
                                ]

                                ]
                            )

    def check(resp):
        return resp.user == ctx.author and resp.channel == ctx.channel

    resp= await sage.wait_for("button_click", check=check)

    if resp.component.label == "Pirates of Caribbean":
        await ctx.invoke(sage.get_command("play_poc"))
        await msg.delete()
    elif resp.component.label == "Rinkiya ke Papa":
        await ctx.invoke(sage.get_command("play_rkp"))
        await msg.delete()
    elif resp.component.label == "Jeena Jeena":
        await ctx.invoke(sage.get_command("play_jj"))
        await msg.delete()
    elif resp.component.label == "Chahun me ya na":
        await ctx.invoke(sage.get_command("play_cmyn"))
        await msg.delete()
    elif resp.component.label == "Last Day On Earth":
        await ctx.invoke(sage.get_command("play_bb"))
        await msg.delete()
    elif resp.component.label == "Lovely":
        await ctx.invoke(sage.get_command("play_lov"))
        await msg.delete()
    else:
      return