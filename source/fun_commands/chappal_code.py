import discord
from ..boot import *
from discord.ext import commands


@sage.listen("on_message")
async def on_message(message):
    if "my slippers" in message.content:
        await message.channel.send(message.author.mention+" Here are your slippers!", file= discord.File("././assets/pictures/chappal.png"))


    if "meri chappal" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"))
        
   
    if "My slippers" in message.content:
        await message.channel.send(message.author.mention+"Here are your slipper!", file= discord.File("././assets/pictures/chappal.png"))
        
    
    if "meri chappale" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"))
       
    
    if "chappal kaha" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"))
        
      
    if "Chappal kaha" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"))
       
        
    if "Chappale kaha" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi Aapi Chappale!", file= discord.File("././assets/pictures/chappal.png"))
       
        
    if "chappale kaha" in message.content:
        await message.channel.send(message.author.mention+" Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"))