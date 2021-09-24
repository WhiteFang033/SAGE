import asyncio
import discord
from ..boot import *
from discord.ext import commands
from discord.utils import *
from discord_components import *


@sage.command()
async def roles(ctx):
    if ctx.channel.id != 830469077951840266:
        return
    await ctx.message.delete()
    msg= await ctx.send("**You can assign/remove roles by clicking on the buttons below:**",
                    components=[[Button(style= ButtonStyle.blue ,label="Assign Role(s)"), 
                                 Button(style= ButtonStyle.red ,label="Remove Role(s)")]]
                  )
    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel
    try:
     res= await sage.wait_for("button_click", check= check, timeout = 20)
    except asyncio.TimeoutError:
          timeout=await ctx.send("**Time Out!**")
          await msg.delete()
          await asyncio.sleep(5)
          await timeout.delete()
          return
    

    if res.component.label== "Assign Role(s)":
        member=ctx.author
        verified= discord.utils.find(
        lambda r: r.name == "Verified", ctx.message.guild.roles
        )
        if verified in member.roles:
          await res.respond(content="**You already have one of the four color roles.**")
          await msg.delete()
    
        else:
           await res.respond(content="**Assigning Roles!**")
           await msg.delete()
           await ctx.invoke(sage.get_command('roles_assigner'))
           
           
     
    if res.component.label== "Remove Role(s)":
        member=ctx.author
        verified= discord.utils.find(
        lambda r: r.name == "Verified", ctx.message.guild.roles
        )
        if verified in member.roles:
           await res.respond(content="**Removing Roles!**")
           await msg.delete()
           await ctx.invoke(sage.get_command('roles_remover'))
    
        else:
          await res.respond(content="**You don't have one of the four color roles.**")
          await msg.delete()
        


@sage.command()
async def roles_assigner(ctx):

    
    msgroles=await ctx.send("**Choose a role to be assigned:**",
                    components=[[Button(style= ButtonStyle.blue ,label="Blue 🔵"),
                                 Button(style= ButtonStyle.blue ,label="Purple 🟣"),
                                 Button(style= ButtonStyle.blue ,label="Brown 🟤"),
                                 Button(style= ButtonStyle.blue ,label="Green 🟢")
                                ]]
                            )
    def check(resp):
     return ctx.author == resp.user and resp.channel == ctx.channel
    try:
         resp= await sage.wait_for("button_click", check= check, timeout = 20)
    except asyncio.TimeoutError:
           tot=await ctx.send("**Time Out!**")
           await asyncio.sleep(2)
           await msgroles.delete()
           await tot.delete()
           return
    verified= get(ctx.author.guild.roles, name="Verified")
    
    if resp.component.label== "Green 🟢":
        member= ctx.author
        mrole= discord.utils.find(
         lambda r: r.name == "green", ctx.message.guild.roles
        )
   
        green= get(member.guild.roles, name="green")
    
        if mrole in member.roles:
           await resp.respond(content="**You already have Green 🟢 role.**")
           await  asyncio.sleep(2)
           await msgroles.delete()
        else:
           await member.add_roles(green)
           await member.add_roles(verified)
           await resp.respond(content="**You got Green 🟢 role!**")
           await asyncio.sleep(2)
           await msgroles.delete()
           return
    
       
    elif resp.component.label== "Blue 🔵":
        member= ctx.author
        mrole= discord.utils.find(
        lambda r: r.name == "blue", ctx.message.guild.roles
        )
        blue= get(member.guild.roles, name="blue")
        if mrole in member.roles:
          await resp.respond(content="**You already have Blue 🔵 role.**")
          await  asyncio.sleep(2)
          await msgroles.delete()
        else:
           await member.add_roles(blue)
           await member.add_roles(verified)
           await resp.respond(content="**You got Blue 🔵 role!**")
           await asyncio.sleep(2)
           await msgroles.delete()
           return

    elif resp.component.label== "Purple 🟣":
        member= ctx.author
        mrole= discord.utils.find(
         lambda r: r.name == "purple", ctx.message.guild.roles
        )
   
        purple= get(member.guild.roles, name="purple")
        if mrole in member.roles:
           await resp.respond(content="**You already have Purple 🟣 role.**")
           await  asyncio.sleep(2)
           await msgroles.delete()
        else:
           await member.add_roles(purple)
           await member.add_roles(verified)
           await resp.respond(content="**You got Purple 🟣 role!**")
           await asyncio.sleep(2)
           await msgroles.delete()
           return
    
    elif resp.component.label== "Brown 🟤":
        member= ctx.author
        mrole= discord.utils.find(
         lambda r: r.name == "brown", ctx.message.guild.roles
        )
        brown= get(member.guild.roles, name="brown")
    
        if mrole in member.roles:
           await resp.respond(content="**You already have Brown 🟤 role.**")
           await  asyncio.sleep(2)
           await msgroles.delete()
        else:
            await member.add_roles(brown)
            await member.add_roles(verified)
            await resp.respond(content="**You got Brown 🟤 role!**")
            await asyncio.sleep(2)
            await msgroles.delete()
            return
    else:
        return

@sage.command()
async def roles_remover(ctx):

    
    msgroles=await ctx.send("**Choose a role to be removed:**",
                    components=[[Button(style= ButtonStyle.blue ,label="Blue 🔵"),
                                 Button(style= ButtonStyle.blue ,label="Purple 🟣"),
                                 Button(style= ButtonStyle.blue ,label="Brown 🟤"),
                                 Button(style= ButtonStyle.blue ,label="Green 🟢")
                                ]]
                            )
    def check(resp):
     return ctx.author == resp.user and resp.channel == ctx.channel
    try:
         resp= await sage.wait_for("button_click", check= check, timeout = 20)
    except asyncio.TimeoutError:
           tot=await ctx.send("**Time Out!**")
           await asyncio.sleep(2)
           await msgroles.delete()
           await tot.delete()
           return
    verified= get(ctx.author.guild.roles, name="Verified")
    
    if resp.component.label== "Green 🟢":
        member= ctx.author
        mrole= discord.utils.find(
         lambda r: r.name == "green", ctx.message.guild.roles
        )
   
        green= get(member.guild.roles, name="green")
    
        if mrole in member.roles:
           await member.remove_roles(green)
           await member.remove_roles(verified)
           await resp.respond(content="**Green 🟢 role removed!**")
           await asyncio.sleep(2)
           await msgroles.delete()
           return
        else:
           await resp.respond(content="**You don't have the Green 🟢 role!**")
           await  asyncio.sleep(2)
           await msgroles.delete()
    
       
    elif resp.component.label== "Blue 🔵":
        member= ctx.author
        mrole= discord.utils.find(
        lambda r: r.name == "blue", ctx.message.guild.roles
        )
        blue= get(member.guild.roles, name="blue")
        if mrole in member.roles:
           await member.remove_roles(blue)
           await member.remove_roles(verified)
           await resp.respond(content="**Blue 🔵 role removed!**")
           await asyncio.sleep(2)
           await msgroles.delete()
           return
        
        else:
           await resp.respond(content="**You don't have the Blue 🔵 role.**")
           await  asyncio.sleep(2)
           await msgroles.delete()
          

    elif resp.component.label== "Purple 🟣":
        member= ctx.author
        mrole= discord.utils.find(
         lambda r: r.name == "purple", ctx.message.guild.roles
        )
   
        purple= get(member.guild.roles, name="purple")
        if mrole in member.roles:
           await member.add_roles(purple)
           await member.add_roles(verified)
           await resp.respond(content="**Purple 🟣 role removed!**")
           await asyncio.sleep(2)
           await msgroles.delete()
           
        else:
           await resp.respond(content="**You don't have the Purple 🟣 role.**")
           await  asyncio.sleep(2)
           await msgroles.delete()
           return
    
    elif resp.component.label== "Brown 🟤":
        member= ctx.author
        mrole= discord.utils.find(
         lambda r: r.name == "brown", ctx.message.guild.roles
        )
        brown= get(member.guild.roles, name="brown")
    
        if mrole in member.roles:
            await member.add_roles(brown)
            await member.add_roles(verified)
            await resp.respond(content="**Brown 🟤 role removed!**")
            await asyncio.sleep(2)
            await msgroles.delete()
            return
        else:
           await resp.respond(content="**You don't have Brown 🟤 role.**")
           await  asyncio.sleep(2)
           await msgroles.delete()
    else:
        return
