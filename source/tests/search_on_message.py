from ..boot import *
import requests
import json



replies = ['I have no idea about that. :confused:',"I do not know that yet :no_mouth:", "Beats me lol.", "I have no knowledge about that thing.:sob:", "I guess I won't be able to help you with that. :confused:"]

@sage.listen("on_message")
async def on_message(message):
    if "Sage" in message.content or "sage" in message.content and "?" in message.content:
        content = message.content
        query = content.replace("Sage,","").replace("sage,","").replace("sage?","").replace("Sage?","")

        ###API
        ##Search_API

        url_search = f"https://google-search3.p.rapidapi.com/api/v1/search/q={query}"

        headers = {
          'x-user-agent': "desktop",
          'x-proxy-location': "US",
          'x-rapidapi-host': "google-search3.p.rapidapi.com",
          'x-rapidapi-key': "a7202c6505mshac4812d4e1434b3p1e7c3bjsn26341f464af9"
        }

        response_search = requests.request("GET", url_search, headers=headers)
        data= json.loads(response_search.text)
        title=data["results"][2]["title"]
        description=data["results"][2]["description"]

        ##Image_API

        url_image = f"https://google-search3.p.rapidapi.com/api/v1/images/q={query}"

        headers = {
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': "a7202c6505mshac4812d4e1434b3p1e7c3bjsn26341f464af9"
            }

        response_image = requests.request("GET", url_image, headers=headers)
        data_image = json.loads(response_image.text)
        image= data_image["image_results"][2]["image"]["src"]
        
        #Search_Result
        
        embed = discord.Embed(title= title, description= description, color=0x2B9CFF)
        embed.set_thumbnail(url=image)
        avatar = message.author.avatar_url
        embed.set_footer(text=f"Searched by {message.author.name}",icon_url=avatar)
        await message.reply(embed=embed)
    

