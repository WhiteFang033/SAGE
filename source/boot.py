import discord 
from discord.ext import commands
import tokens

intents = discord.Intents.all()
sage = commands.Bot(command_prefix="!", intents= intents, help_command=None)

@sage.event
async def on_ready():
    await sage.change_presence(status= discord.Status.dnd, activity= discord.Game('Shinra Tensei'))
    print("Sage is Online.")
 
def run():
    sage.run(tokens.sage_token)