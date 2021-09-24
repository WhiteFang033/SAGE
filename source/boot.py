import discord 
from discord.ext import commands
from discord_components import *

intents = discord.Intents.all()
sage = commands.Bot(command_prefix="!", intents= intents)

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

@sage.event
async def on_ready():
    await sage.change_presence(status= discord.Status.idle, activity= discord.Game('Shinra Tensei'))
    DiscordComponents(sage)
    print("Sage is Online.")
 
def run():
    sage.run("ODcyMDI0MTg4NDc3NjY5NDE2.YQj1zw.RcNROsYGP4afhGZaTC__eA7Xors")