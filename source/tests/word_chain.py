from typing import AsyncContextManager
from ..boot import *





@sage.listen("on_message")
async def on_message(i_message):
    global i_last_w
    global digit

    if i_message.channel.id == 875733240902742027:
       digit, word = i_message.content.split(".")
       print(digit)
       print(word)
       i_last_w = word[-1]

@sage.listen("on_message")
async def on_message(f_message):

    f_digit, f_word = f_message.content.split(".")
    print(f_digit), print(f_word)
    first_w = f_word[0]
    if first_w != i_last_w or int(f_digit) != int(digit)+1:
      await  f_message.delete()
      
      