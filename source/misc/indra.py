import discord
from discord import activity
from discord.enums import Status
from discord.ext import commands
import tokens

activity = discord.CustomActivity("Jai")
indra = commands.Bot(command_prefix="-", Status = discord.Status.dnd, activity =activity)

@indra.event
async def on_ready():
    
    print("Indra is online")

indra.run(tokens.indra_token)


