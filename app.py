#!/usr/bin/python3
import discord
from functions import *


# code....


# getToken() function callback (to store the token as variable).
TOKEN = getToken()
PREFIX = getPrefix()

# print(TOKEN)
class MatchingBot(discord.Client):
    async def on_ready(self):
        print(f"Bot is started as {self.user}!")
    async def on_message(self, message):
        if message.content == PREFIX + "profile":
            await message.channel.send(splitRoles([str(i.name) for i in message.author.roles]))

client = MatchingBot()

client.run(TOKEN)