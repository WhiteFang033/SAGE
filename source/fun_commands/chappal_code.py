import discord
from ..boot import *
from discord.ext import commands


@sage.listen("on_message")
async def on_message(message):
    if "my slippers" in message.content:
        await message.channel.send(message.author.mention+" Here are your slippers!", file= discord.File("././assets/pictures/chappal.png"),components= [[Button(style= ButtonStyle.green, label="Slipper Smack"),
                                                                                                                                    Button(style= ButtonStyle.blue, label="Make a Chase")]])
        def check(resp):
         return message.author==resp.user and resp.channel==message.channel
        resp= await sage.wait_for("button_click", check=check)
            
        if resp.component.label == "Slipper Smack":
                await message.channel.send("Slipper Smacking...")
                await message.channel.send("https://tenor.com/view/distance-angry-mother-mom-flip-flops-gif-19998748")
        
        elif resp.component.label == "Make a Chase":
            await message.channel.send("Chasing...")
            await message.channel.send("https://tenor.com/view/slipper-beat-run-chase-gif-17899015")
        else:
            return



    if "meri chappal" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"),components= [[Button(style= ButtonStyle.green, label="Slipper Smack"),
                                                                                                                                    Button(style= ButtonStyle.blue, label="Make a Chase")]])
        def check(resp):
         return message.author==resp.user and resp.channel==message.channel
        resp= await sage.wait_for("button_click", check=check)
            
        if resp.component.label == "Slipper Smack":
                await message.channel.send("Slipper Smacking...")
                await message.channel.send("https://tenor.com/view/distance-angry-mother-mom-flip-flops-gif-19998748")
        
        elif resp.component.label == "Make a Chase":
            await message.channel.send("Chasing...")
            await message.channel.send("https://tenor.com/view/slipper-beat-run-chase-gif-17899015")
        else:
            return
   
    if "My slippers" in message.content:
        await message.channel.send(message.author.mention+"Here are your slipper!", file= discord.File("././assets/pictures/chappal.png"),components= [[Button(style= ButtonStyle.green, label="Slipper Smack"),
                                                                                                                                    Button(style= ButtonStyle.blue, label="Make a Chase")]])
        def check(resp):
         return message.author==resp.user and resp.channel==message.channel
        resp= await sage.wait_for("button_click", check=check)
            
        if resp.component.label == "Slipper Smack":
                await message.channel.send("Slipper Smacking...")
                await message.channel.send("https://tenor.com/view/distance-angry-mother-mom-flip-flops-gif-19998748")
        
        elif resp.component.label == "Make a Chase":
            await message.channel.send("Chasing...")
            await message.channel.send("https://tenor.com/view/slipper-beat-run-chase-gif-17899015")
        else:
            return
    
    if "meri chappale" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"),components= [[Button(style= ButtonStyle.green, label="Slipper Smack"),
                                                                                                                                    Button(style= ButtonStyle.blue, label="Make a Chase")]])
        def check(resp):
         return message.author==resp.user and resp.channel==message.channel
        resp= await sage.wait_for("button_click", check=check)
            
        if resp.component.label == "Slipper Smack":
                await message.channel.send("Slipper Smacking...")
                await message.channel.send("https://tenor.com/view/distance-angry-mother-mom-flip-flops-gif-19998748")
        
        elif resp.component.label == "Make a Chase":
            await message.channel.send("Chasing...")
            await message.channel.send("https://tenor.com/view/slipper-beat-run-chase-gif-17899015")
        else:
            return
    
    if "chappal kaha" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"),components= [[Button(style= ButtonStyle.green, label="Slipper Smack"),
                                                                                                                                    Button(style= ButtonStyle.blue, label="Make a Chase")]])
        def check(resp):
         return message.author==resp.user and resp.channel==message.channel
        resp= await sage.wait_for("button_click", check=check)
            
        if resp.component.label == "Slipper Smack":
                await message.channel.send("Slipper Smacking...")
                await message.channel.send("https://tenor.com/view/distance-angry-mother-mom-flip-flops-gif-19998748")
        
        elif resp.component.label == "Make a Chase":
            await message.channel.send("Chasing...")
            await message.channel.send("https://tenor.com/view/slipper-beat-run-chase-gif-17899015")
        else:
            return
      
    if "Chappal kaha" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"),components= [[Button(style= ButtonStyle.green, label="Slipper Smack"),
                                                                                                                                    Button(style= ButtonStyle.blue, label="Make a Chase")]])
        def check(resp):
         return message.author==resp.user and resp.channel==message.channel
        resp= await sage.wait_for("button_click", check=check)
            
        if resp.component.label == "Slipper Smack":
                await message.channel.send("Slipper Smacking...")
                await message.channel.send("https://tenor.com/view/distance-angry-mother-mom-flip-flops-gif-19998748")
        
        elif resp.component.label == "Make a Chase":
            await message.channel.send("Chasing...")
            await message.channel.send("https://tenor.com/view/slipper-beat-run-chase-gif-17899015")
        else:
            return
        
    if "Chappale kaha" in message.content:
        await message.channel.send(message.author.mention+"Ye rahi Aapi Chappale!", file= discord.File("././assets/pictures/chappal.png"),components= [[Button(style= ButtonStyle.green, label="Slipper Smack"),
                                                                                                                                    Button(style= ButtonStyle.blue, label="Make a Chase")]])
        def check(resp):
         return message.author==resp.user and resp.channel==message.channel
        resp= await sage.wait_for("button_click", check=check)
            
        if resp.component.label == "Slipper Smack":
                await message.channel.send("Slipper Smacking...")
                await message.channel.send("https://tenor.com/view/distance-angry-mother-mom-flip-flops-gif-19998748")
        
        elif resp.component.label == "Make a Chase":
            await message.channel.send("Chasing...")
            await message.channel.send("https://tenor.com/view/slipper-beat-run-chase-gif-17899015")
        else:
            return
        
    if "chappale kaha" in message.content:
        await message.channel.send(message.author.mention+" Ye rahi aapki chappale!", file= discord.File("././assets/pictures/chappal.png"),components= [[Button(style= ButtonStyle.green, label="Slipper Smack"),
                                                                                                                                    Button(style= ButtonStyle.blue, label="Make a Chase")]])
        def check(resp):
         return message.author==resp.user and resp.channel==message.channel
        resp= await sage.wait_for("button_click", check=check)
            
        if resp.component.label == "Slipper Smack":
                await message.channel.send("Slipper Smacking...")
                await message.channel.send("https://tenor.com/view/distance-angry-mother-mom-flip-flops-gif-19998748")
        
        elif resp.component.label == "Make a Chase":
            await message.channel.send("Chasing...")
            await message.channel.send("https://tenor.com/view/slipper-beat-run-chase-gif-17899015")
        else:
            return