import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
client_id = os.getenv("CLIENT_ID")


class KodaBot(discord.Client):
    version = '0.0.1'

    def __init__(self, Debug=None, ):
        self.Debug = Debug

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print('Versão Discord:', discord.__version__)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = KodaBot()
client.run(token)
