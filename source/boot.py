import discord 
from discord.ext import commands

intents = discord.Intents.all()
sage = commands.Bot(command_prefix="!", intents= intents, help_command=None)

@sage.event
async def on_ready():
    await sage.change_presence(status= discord.Status.dnd, activity= discord.Game('Shinra Tensei'))
    print("Sage is Online.")
 
def run():
    sage.run("ODcyMDI0MTg4NDc3NjY5NDE2.YQj1zw.RcNROsYGP4afhGZaTC__eA7Xors")