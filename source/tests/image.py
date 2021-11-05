from ..boot import *
from PIL import Image, ImageDraw, ImageFont
import os
import requests
from io import BytesIO

@sage.command()
async def flip(ctx):
    url = ctx.message.attachments[0].url
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    fimg = img.transpose(Image.FLIP_LEFT_RIGHT)

    fimg.save("flipped.png")
    await ctx.send(file=discord.File("flipped.png"))

@sage.command()
async def rotate(ctx):
    print(ctx.message.attachments)
    url = ctx.message.attachments[0].url
    
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    fimg = img.transpose(Image.ROTATE_90)

    fimg.save("flipped.png")
    await ctx.send(file=discord.File("flipped.png"))
    os.remove("../../flipped.png")
