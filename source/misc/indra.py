import discord
from discord import activity
from discord.enums import Status
from discord.ext import commands


activity = discord.CustomActivity("Jai")
indra = commands.Bot(command_prefix="-", Status = discord.Status.dnd, activity =activity)

@indra.event
async def on_ready():
    
    print("Indra is online")

indra.run("ODk0NTE3NTU0ODM4NjM0NTA3.YVrKZA.00W7XgRaCq6rWIZWdANbzMMq_C8")


