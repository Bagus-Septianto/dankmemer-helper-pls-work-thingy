import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client(status=discord.Status.dnd)

# 270904126974590976 is dankmemer's id

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Check if the message author is dankmemer
    if message.author.id == 270904126974590976:
        # Repeat Order
        # Copy-Paste the message
        if 'remember words order!' in message.content.lower():
            await message.channel.send(message.content)

        # Emoji Match
        # Copy-Paste the emoji that needs to be remembered
        if 'look at the emoji closely!' in message.content.lower():
            target = message.content.split('\n')
            target = target[1]
            await message.channel.send(target)

@client.event
async def on_message_edit(message_before, message_after):
    # Check if the message author is dankmemer
    if message_before.author.id == 270904126974590976:
        # print all emoji according to the order (5x2 or smt. idk, try urself)
        if 'What was the emoji?' in message_after.content:
            message_to_send = ''
            if not message_after.components[0].children[0].disabled:
                for component in message_after.components:
                    for btn in component.children:
                        message_to_send = message_to_send + str(btn.emoji.name)
                    message_to_send = message_to_send + '\n'
                await message_after.channel.send(message_to_send)

        # print the correct color
        if 'What color was next to the word' in message_after.content:
            target = message_after.content.split('`')
            target = target[1]
            sources = message_before.content.split(':')
            for idx, source in enumerate(sources):
                if target in source: # i am using 'in' because the source has \n or spaces & i am lazy to do smt abt it
                    color = sources[idx-1]
            if not message_after.components[0].children[0].disabled: # if the button is not disabled then send the message
                await message_after.channel.send(color)

client.run(token)
