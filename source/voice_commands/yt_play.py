import discord
from ..boot import *
import requests
import json

@sage.command(aliases= ['yp'])
async def search_music(ctx, keyword):
    url = "https://youtube-search-results.p.rapidapi.com/youtube-search/"

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


    await ctx.reply(f"``Results: {title}`` \n {link}")

