from ..boot import *

@sage.command()
async def hack(ctx, member: discord.Member):
    await ctx.send(f"``Hacking {member}'s account'...``")
    msg= await ctx.send(f"``Hacking {member}'s account'...``")
    bar = "█"
    progress_bar = "█"
    loading= await ctx.send(progress_bar)

    for x in range(101):
        
         

        if x == 100:
            await msg.edit(content="``Task failed successfully.✔")
        else:
            await msg.edit(content= f"``Hacking...{x}%``")
            await loading.edit(content=f"{progress_bar}")
            progress_bar = progress_bar+ bar

