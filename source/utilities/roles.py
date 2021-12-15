import asyncio
import discord
from ..boot import *
from discord.ext import commands
from discord.utils import *
from discord_components import *

@sage.command()
@commands.has_any_role(830439735050371103)
async def roles_menu(ctx):

    
    msgroles=await ctx.send("**Hey There, Welcome to the Server HiddenLeaf.** \n\nYou can have any of the four-color roles which makes your profile look colorful!\nSelect the interaction buttons to assign/remove the respective roles:\n\n👉 Choose **Cyan** for the <@&830491828326891520> role.\n👉 Choose **Purple** for the <@&830492214106128434> role.\n👉 Choose **Blue** for the <@&830492103347666956> role.\n👉 Choose **Green** for the <@&830492400039231508> role.\n \n**Thank You!**",
                    components=[[Button(style= ButtonStyle.blue ,label="Cyan"),
                                 Button(style= ButtonStyle.blue ,label="Purple"),
                                 Button(style= ButtonStyle.blue ,label="Blue"),
                                 Button(style= ButtonStyle.blue ,label="Green")
                                ]]
                            )


    
    def check(resp):
       return resp.channel == ctx.channel
    
    while(True): 
      resp= await sage.wait_for("button_click", check= check)

      if resp.component.label== "Cyan":
          member= ctx.author
          mrole= discord.utils.find(
           lambda r: r.name == "cyan", ctx.message.guild.roles
          )

          verified= get(member.guild.roles, name="Verified")
   
          cyan= get(member.guild.roles, name="cyan")
    
          if mrole in member.roles:
             await member.remove_roles(cyan)
             await resp.respond(content="**Cyan role removed.**")
          else:
             await member.add_roles(cyan)
             await member.add_roles(verified)
             await resp.respond(content="**You got the Cyan role!**")
            
    
       
      elif resp.component.label== "Blue":
          member= ctx.author
          mrole= discord.utils.find(
          lambda r: r.name == "blue", ctx.message.guild.roles
          )
          verified= get(member.guild.roles, name="Verified")
          blue= get(member.guild.roles, name="blue")
          if mrole in member.roles:
            await member.remove_roles(blue)
            await resp.respond(content="**Blue role removed.**")
          else:
             await member.add_roles(blue)
             await member.add_roles(verified)
             await resp.respond(content="**You got the Blue role!**")

      elif resp.component.label== "Purple":
          member= ctx.author
          mrole= discord.utils.find(
           lambda r: r.name == "purple", ctx.message.guild.roles
          )
          verified= get(member.guild.roles, name="Verified")
   
          purple= get(member.guild.roles, name="purple")
          if mrole in member.roles:
             await member.remove_roles(purple)
             await resp.respond(content="**Purple role removed.**")
          else:
             await member.add_roles(purple)
             await member.add_roles(verified)
             await resp.respond(content="**You got the Purple role!**")
             
    
      elif resp.component.label== "Green":
          member= ctx.author
          mrole= discord.utils.find(
           lambda r: r.name == "green", ctx.message.guild.roles
          )
          verified= get(member.guild.roles, name="Verified")
          green= get(member.guild.roles, name="green")
      
          if mrole in member.roles:
             await member.remove_roles(green)
             await resp.respond(content="**Green role removed.**")
          else:
              await member.add_roles(green)
              await member.add_roles(verified)
              await resp.respond(content="**You got the Green role!**")