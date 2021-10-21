import discord
from discord.ext import commands

indra = commands.Bot(command_prefix="-")

@indra.event
async def on_ready():
    await indra.change_presence(status=discord.Status.dnd, activity=discord.Game("Interstellar"))
    print("Indra is online")

indra.run("ODk0NTE3NTU0ODM4NjM0NTA3.YVrKZA.00W7XgRaCq6rWIZWdANbzMMq_C8")


