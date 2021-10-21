from ..boot import *
from PIL import Image, ImageDraw, ImageFont
import os
import requests
from io import BytesIO

@sage.command()
async def show(ctx):

    member = ctx.author

    avatar =member.avatar_url
    response =requests.get(avatar)

    ava= Image.open(BytesIO(response.content))
    text = member.name

    fw= Image.new("RGB",(600,300),color="black")
    d= ImageDraw.Draw(fw)
    font = ImageFont.truetype("../../assets/fonts/arial.ttf",50)
    d.text((300,150),text,fill=(256,256,256), font= font)
    fw.save("black.png")
    await ctx.reply(file= discord.File(ava))

    os.remove("black.png")
