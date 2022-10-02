import discord
from ..boot import *
from gtts import gTTS
import os

@sage.command()
async def speak(ctx,lang ="en",*,message):
    text = message
    language = lang
    vmsg = gTTS(text=message, lang=language, slow=False)
    vmsg.save('voice_message.mp3')
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    f_vmsg = discord.FFmpegPCMAudio('voice_message.mp3')
    voice.play(f_vmsg)
    

    
    