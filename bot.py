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
        await message.channel.send('dizes', tts=False)

    if message.content.startswith("!megadizes"):
        await message.channel.send('''\
    ```

    .___.__                      
  __| _/|__|_______ ____   ______
 / __ | |  \___   // __ \ /  ___/
/ /_/ | |  |/    /\  ___/ \___ \ 
\____ | |__/_____ \\___  >____  >
     \/          \/    \/     \/ 

```''')


client.run(TOKEN)
