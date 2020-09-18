#!/usr/bin/python3
import discord
from functions import *

# getToken() function callback (to store the token as variable).
TOKEN = getToken()
PREFIX = getPrefix()
PREFERS = getPrefers()

class MatchingBot(discord.Client):
    
    # Signing bot starting.
    async def on_ready(self):
        print(f"Bot is started as {self.user}!")

    # Get profile function.
    async def on_message(self, message):
        if message.content == PREFIX + "profile":
            data = splitRoles([str(i.name) for i in message.author.roles])
            if data != "Complete your profile please.":
                embed = discord.Embed(title=f"{message.author}",color=discord.Colour(0xda2222))
                embed.set_author(name="ShinySuger", icon_url="https://i.imgur.com/h1ptNUR.png")
                embed.set_thumbnail(url=f"{message.author.avatar_url}")
                embed.add_field(name="Region", value=f"{arrtoText(data['regions'])}", inline=True)
                embed.add_field(name="Gendre", value=f"{arrtoText(data['gendre'])}", inline=True)
                embed.add_field(name="Likes", value=f"{arrtoText(data['likes'])}", inline=True)
                embed.add_field(name="Sexuality", value=f"{arrtoText(data['sexuality'])}", inline=True)
                embed.add_field(name="Age", value=f"{arrtoText(data['ages'])}", inline=True)
                embed.add_field(name="Statue", value=f"{arrtoText(data['statue'])}", inline=True)
                embed.add_field(name="Prefer", value=f"{arrtoText(data['prefers'])}", inline=True)
                embed.set_footer(text="ShinySuger - https://discord.gg/q3axBYW")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(data)

    # Match function
    async def on_message(self, message):
        if message.content == PREFIX + "match":
            data = splitRoles([str(i.name) for i in message.author.roles])
            if data != "Complete your profile please.":
                if arrtoText(data['sexuality']) in PREFERS:
                    await message.channel.send(f"Oh! You Prefer {PREFERS[arrtoText(data['sexuality'])][arrtoText(data['prefers'])]}")
            else:
                    await message.channel.send(data)

                        

client = MatchingBot()

client.run(TOKEN)