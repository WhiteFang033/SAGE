import discord
from ..boot import *
from .voice import *
from discord.ext import commands
from .music_menu import *

@sage.command()
async def play_poc(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    poc= discord.FFmpegPCMAudio('media/mp3/Alpha/poc.mp3',)
    voice.play(poc)


@sage.command()
async def play_jj(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    jj= discord.FFmpegPCMAudio('media/mp3/Alpha/jj.mp3',)
    voice.play(jj)

@sage.command()
async def play_rkp(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    rkp= discord.FFmpegPCMAudio('media/mp3/Alpha/rkp.mp3',)
    voice.play(rkp)
    
@sage.command()
async def play_cmyn(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    cmyn= discord.FFmpegPCMAudio('media/mp3/Alpha/.mp3',)
    voice.play(cmyn)

@sage.command()
async def play_pw(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    pw= discord.FFmpegPCMAudio('media/mp3/Alpha/pw.mp3',)
    voice.play(pw)

@sage.command()
async def play_bb(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    bb= discord.FFmpegPCMAudio('media/mp3/Alpha/bb.mp3',)
    voice.play(bb)

@sage.command()
async def play_lov(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    lovely= discord.FFmpegPCMAudio('media/mp3/Alpha/lovely.mp3',)
    voice.play(lovely)

@sage.command()
async def play_byebye(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    byebye= discord.FFmpegPCMAudio('media/mp3/Alpha/bye bye.mp3',)
    voice.play(byebye)

    