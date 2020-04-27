# import json
# import requests
import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
client_id = os.getenv("CLIENT_ID")

print(f"TOKEN: {token}\n"
      f"CLIENT_ID: {client_id}")

client = discord.Client()


@client.event
async def on_ready():
    print('Eu loguei no {0.user}', format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')


client.run(token)
