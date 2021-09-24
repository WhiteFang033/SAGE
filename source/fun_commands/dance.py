import asyncio
import discord
from ..boot import *
from discord.ext import commands

@sage.command()
async def dance(ctx):
    await ctx.reply("LET'S START")
    await ctx.send("PLAY MUSIC 🎶")
    await asyncio.sleep(3)
    await ctx.send("https://tenor.com/view/indian-guy-gif-5337959")
    await asyncio.sleep(5)
    await ctx.send("https://tenor.com/view/indian-dance-dance-dancing-dance-party-india-gif-20598542")
    await asyncio.sleep(7)
    await ctx.send("https://tenor.com/view/nikaru22-dancing-uncle-swag-baarat-celebration-gif-19486487")
    await asyncio.sleep(7)
    await ctx.send("Pary Over... Go Home Now.")
    await asyncio.sleep(2)
    await ctx.send("https://tenor.com/view/extinguished-partys-over-done-birthday-cake-gif-9191862")

@dance.error
async def dance(ctx, error):
    message = error
    await ctx.reply(message)