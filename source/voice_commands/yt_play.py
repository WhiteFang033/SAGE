import datetime
import asyncio
import discord
from .voice import *
from discord.ext.commands.core import check
from ..boot import *
import requests
import json
import youtube_dl 
import asyncio


youtube_dl.utils.bug_reports_message = lambda: ''

msg= ''
status=''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)








@sage.command(aliases= ['p'])
async def play_music(ctx,*,keyword):
     
    url = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
    
    print(keyword)

    querystring = {"q":keyword}

    headers = {
     'x-rapidapi-host': "youtube-search-results.p.rapidapi.com",
     'x-rapidapi-key': "a7202c6505mshac4812d4e1434b3p1e7c3bjsn26341f464af9"
       }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data = json.loads(response.text)
    items= data["items"] 
    link = items[0]["url"] 
    title = items[0]["title"] 
    thumbnail = items[0]["bestThumbnail"]["url"] 
    duration = items[0]["duration"] 

    if len(duration)<=4:
      str = "00:"+duration
  
    print(str)
    h,m,s = str.split(':')


    time = int(h)*3600 + int(m)*60 + int(s)

    print(f"time= {time} seconds")

    voice= discord.utils.get(sage.voice_clients, guild= ctx.guild)

    embed = discord.Embed(title=f"Playing", description = f"**Now Playing- **{title} \n **Duration- **{duration} ", color=0x2B9CFF)
    embed.set_image(url=thumbnail)


    msg= await ctx.reply(embed = embed)



    async with ctx.typing():
        player = await YTDLSource.from_url(link)
        voice.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    status= await ctx.send("``Status: 🎶Playing``")

@play_music.error
async def search_music(ctx,error):
    message = error
    await ctx.reply(message)

  

    

     