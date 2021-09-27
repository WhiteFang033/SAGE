import discord
from ..boot import *
from .voice import *
from discord.ext import commands
from .music_menu import *

@sage.command()
async def play_poc(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    poc= discord.FFmpegPCMAudio('media/mp3/alpha/poc.mp3')
    voice.play(poc)


@sage.command()
async def play_jj(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    jj= discord.FFmpegPCMAudio('media/mp3/alpha/jj.mp3')
    voice.play(jj)

@sage.command()
async def play_rkp(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    rkp= discord.FFmpegPCMAudio('media/mp3/alpha/rkp.mp3')
    voice.play(rkp)
    
@sage.command()
async def play_cmyn(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    cmyn= discord.FFmpegPCMAudio('media/mp3/alpha/.mp3')
    voice.play(cmyn)

@sage.command()
async def play_pw(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    pw= discord.FFmpegPCMAudio('media/mp3/alpha/pw.mp3')
    voice.play(pw)

@sage.command()
async def play_bb(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    bb= discord.FFmpegPCMAudio('media/mp3/alpha/bb.mp3')
    voice.play(bb)

@sage.command()
async def play_lov(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    lovely= discord.FFmpegPCMAudio('media/mp3/alpha/lovely.mp3')
    voice.play(lovely)

@sage.command()
async def play_byebye(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    byebye= discord.FFmpegPCMAudio('media/mp3/alpha/bye bye.mp3')
    voice.play(byebye)

@sage.command()
async def play_ab(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio('media/mp3/beta/Angel Baby.mp3')
    voice.play(music)

@sage.command()
async def play_hyp(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio("media/mp3/beta/Here's Your Perfect.mp3")
    voice.play(music)

@sage.command()
async def play_dbtake(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio('media/mp3/beta/Double Take.mp3')
    voice.play(music)

@sage.command()
async def play_iml(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio("media/mp3/beta/I GUESS I'M IN LOVE.mp3")
    voice.play(music)

@sage.command()
async def play_mma(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio("media/mp3/beta/Meet Me in Amsterdam.mp3")
    voice.play(music)


#Japanese_music

@sage.command()
async def play_rain(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio("media/mp3/gamma/Rain.mp3")
    voice.play(music)

@sage.command()
async def play_hnara(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio("media/mp3/gamma/Hikaru Nara.mp3")
    voice.play(music)

@sage.command()
async def play_theW(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio("media/mp3/gamma/the WORLD.mp3")
    voice.play(music)

@sage.command()
async def play_nand(ctx):
    voice_channel = ctx.author.voice
    voice= discord.utils.get(sage.voice_clients, guild=ctx.guild)
    music= discord.FFmpegPCMAudio("media/mp3/gamma/Nandemonaiya(Remix).mp3")
    voice.play(music)