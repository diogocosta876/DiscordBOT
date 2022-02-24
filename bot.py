import discord
import random
from config import TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if random.randint(1, 20) == 1:
        await message.channel.send('hey! this is a random response to a message', tts=False)

    if message.content.startswith("!megadizes"):
        await message.channel.send('''\
    ```

888    888 8888888888 Y88b   d88P 
888    888 888         Y88b d88P  
888    888 888          Y88o88P   
8888888888 8888888       Y888P    
888    888 888            888     
888    888 888            888     
888    888 888            888     
888    888 8888888888     888

```''')


client.run(TOKEN)
