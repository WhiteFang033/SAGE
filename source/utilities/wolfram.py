import discord
from ..boot import *
import wolframalpha
import requests
import json


app_id ="VUVX4Q-47T2W8PVHV"


@sage.command(aliases=['w'])
async def wolf(ctx,*, query):

    url= f"https://api.wolframalpha.com/v1/result?appid={app_id}&i={query}%3F"

    response = requests.get(url)
    print(response.text)
    await ctx.reply(f"``RESULTS: {response.text}``")

@wolf.error
async def wolf(ctx, error):
    message = error
    await ctx.reply(message)

@sage.command(aliases=['wi'])
async def wolf_image(ctx,*, query):

    url= f"http://api.wolframalpha.com/v2/query?appid={app_id}&input={query}&includepodid=Image:PeopleData&output=json"

    response = requests.get(url)
    r_json = json.loads(response.text)
    image_url = r_json['queryresult']['pods'][0]['subpods']['img']['src']

    await ctx.reply(f"``RESULTS:\n {image_url}")

@wolf_image.error
async def wolf_image(ctx, error):
    message = error
    await ctx.reply(message)

