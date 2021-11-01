import discord
from ..boot import *
from .music import *
from discord.ext import commands

@sage.command()
async def play_secret_command_pro_max(ctx):
    lang_opt= await ctx.send("**🎶Choose Language:**", 
                    components=[[Button(style= ButtonStyle.green ,label="English🎶"),
                                 Button(style= ButtonStyle.green ,label="Hindi🎶"),
                                 Button(style= ButtonStyle.green ,label="Japanese🎶")
                              ]])
    def check(resp):
        return resp.user == ctx.author and resp.channel == ctx.channel               
    resp= await sage.wait_for("button_click", check=check)                


    if resp.component.label == "English🎶":
      await lang_opt.delete()
      msg= await ctx.send("**🎶Choose a song**", 
                    components=[[Button(style= ButtonStyle.green ,label="Pirates of Caribbean"),
                                 Button(style= ButtonStyle.green ,label="Here's Your Perfect"),
                                 Button(style= ButtonStyle.green ,label="Double Take"),
                                 Button(style= ButtonStyle.green ,label="Angel Baby"),
                                 Button(style= ButtonStyle.green ,label="Last Day On Earth")
                                ],
                                
                                [
                                Button(style= ButtonStyle.green ,label="Lovely"),
                                Button(style= ButtonStyle.green ,label="I GUESS I'M IN LOVE"),
                                Button(style= ButtonStyle.green ,label="Meet Me in Amsterdam")
                                ]

                                ]
                            )

      def check(resp):
        return resp.user == ctx.author and resp.channel == ctx.channel

      resp= await sage.wait_for("button_click", check=check)

      if resp.component.label == "Pirates of Caribbean":
        await ctx.invoke(sage.get_command("play_poc"))
        await msg.delete()
      elif resp.component.label == "Last Day On Earth":
        await ctx.invoke(sage.get_command("play_bb"))
        await msg.delete()
      elif resp.component.label == "Lovely":
        await ctx.invoke(sage.get_command("play_lov"))
        await msg.delete()
      elif resp.component.label == "Here's Your Perfect":
        await ctx.invoke(sage.get_command("play_hyp"))
        await msg.delete()
      elif resp.component.label == "Double Take":
        await ctx.invoke(sage.get_command("play_dbtake"))
        await msg.delete()
      elif resp.component.label == "Angel Baby":
        await ctx.invoke(sage.get_command("play_ab"))
        await msg.delete()
      elif resp.component.label == "I GUESS I'M IN LOVE":
        await ctx.invoke(sage.get_command("play_iml"))
        await msg.delete()
      elif resp.component.label == "Meet Me in Amsterdam":
        await ctx.invoke(sage.get_command("play_mma"))
        await msg.delete()
      else:
       return
    
    elif resp.component.label == "Hindi🎶":
        await lang_opt.delete()
        msg= await ctx.send("**🎶Choose a song**", 
                    components=[[Button(style= ButtonStyle.green ,label="Rinkiya ke Papa"),
                                 Button(style= ButtonStyle.green ,label="Jeena Jeena"),
                                 Button(style= ButtonStyle.green ,label="Chahun me ya na")]])
        def check(resp):
         return resp.user == ctx.author and resp.channel == ctx.channel

        resp= await sage.wait_for("button_click", check=check)

        if resp.component.label == "Rinkiya ke Papa":
          await ctx.invoke(sage.get_command("play_rkp"))
          await msg.delete()
        elif resp.component.label == "Jeena Jeena":
          await ctx.invoke(sage.get_command("play_jj"))
          await msg.delete()
        elif resp.component.label == "Chahun me ya na":
          await ctx.invoke(sage.get_command("play_cmyn"))
          await msg.delete()
        
        else:
         return                         

    elif resp.component.label == "Japanese🎶":
        await lang_opt.delete()
        msg= await ctx.send("**🎶Choose a song**", 
                    components=[[Button(style= ButtonStyle.green ,label="Rain"),
                                 Button(style= ButtonStyle.green ,label="Hikaru Nara"),
                                 Button(style= ButtonStyle.green ,label="the World"),
                                 Button(style= ButtonStyle.green ,label="Nandemonaiya(Remix)")]])
        def check(resp):
         return resp.user == ctx.author and resp.channel == ctx.channel

        resp= await sage.wait_for("button_click", check=check)

        if resp.component.label == "Rain":
          await ctx.invoke(sage.get_command("play_rain"))
          await msg.delete()
        if resp.component.label == "Hikaru Nara":
          await ctx.invoke(sage.get_command("play_hnara"))
          await msg.delete()
        elif resp.component.label == "the World":
          await ctx.invoke(sage.get_command("play_theW"))
          await msg.delete()
        elif resp.component.label == "Nandemonaiya(Remix)":
          await ctx.invoke(sage.get_command("play_nand"))
          await msg.delete()
        
        else:
         return                         

@play_secret_command_pro_max.error
async def play_secret_command_pro_max(ctx,error):
  message = error
  await ctx.reply(message)