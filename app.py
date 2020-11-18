#!/usr/bin/python3

# Bot By ShinySugar
# Aka Jakom, Young, Satan
# Our Discord Server: https://discord.gg/sugar
# Contact Me: Jakom#0002

import discord
import numpy as np
from functions import *
import random

TOKEN = getToken()
PREFIX = getPrefix()

class MatchingBot(discord.Client):
    # Signing bot starting.
    async def on_ready(self):
        print(f"Bot is started as {self.user}!")

    # Get profile function.
    async def on_message(self, message):
        if message.content.lower() == PREFIX + "profile":
            data = splitRoles([i.id for i in message.author.roles])
            if data != "Complete your profile please.":

                for i in data:
                    data[i] = list(map(lambda x: message.guild.get_role(x).name,data[i]))

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
                await message.author.send(embed=embed)
                await message.add_reaction(u"\u2705")
            else:
                await message.author.send("Please complete your profile in #self-roles.")
                await message.add_reaction(u"\U0001F6AB")

        if message.content.lower() == PREFIX + "match":
            data = splitRoles([i.id for i in message.author.roles])
            if data != "Complete your profile please.":
                r__ = {}
                for i in message.guild.get_role(data["sexuality"][0]).members:
                    if splitRoles([j.id for j in i.roles]) != "Complete your profile please." and i.id != message.author.id:
                        r__[str(i.id)] = splitRoles([j.id for j in i.roles])

                if data["prefers"][0] == 753211749104091166:
                    d = 753212261287460865
                else:
                    d = 753212262239698974

                r_r = {}

                for u in r__:
                    if r__[u]["sexuality"][0] == data["sexuality"][0] and r__[u]["gendre"][0] == d:
                        b1 = np.array([i for i in data["likes"]])
                        b2 = [i for i in r__[u]["likes"]]
                        r_r[u] = len(np.intersect1d(b1,b2))
                b_m = {}
                r_r = {k: v for k, v in sorted(r_r.items(), key=lambda item: item[1],reverse=True)}
                n = r_r[list(r_r.keys())[0]]
                for i in r_r:
                    if r_r[i] < n:
                        pass
                    else:
                        b_m[i] = r_r[i]
                r4 = random.choice(list(b_m.keys()))
                c = client.get_user(int(r4))
                for g in r__[r4]:
                    r__[r4][g] = list(map(lambda x: message.guild.get_role(x).name,r__[r4][g]))

                embed = discord.Embed(title=f"{c}",color=discord.Colour(0xda2222))
                embed.set_author(name="ShinySuger", icon_url="https://i.imgur.com/h1ptNUR.png")
                embed.set_thumbnail(url=f"{c.avatar_url}")
                embed.add_field(name="Region", value=f"{arrtoText(r__[r4]['regions'])}", inline=True)
                embed.add_field(name="Gendre", value=f"{arrtoText(r__[r4]['gendre'])}", inline=True)
                embed.add_field(name="Likes", value=f"{arrtoText(r__[r4]['likes'])}", inline=True)
                embed.add_field(name="Sexuality", value=f"{arrtoText(r__[r4]['sexuality'])}", inline=True)
                embed.add_field(name="Age", value=f"{arrtoText(r__[r4]['ages'])}", inline=True)
                embed.add_field(name="Statue", value=f"{arrtoText(r__[r4]['statue'])}", inline=True)
                embed.add_field(name="Prefer", value=f"{arrtoText(r__[r4]['prefers'])}", inline=True)
                embed.set_footer(text="ShinySuger - https://discord.gg/sugar")
                await message.author.send("Best Match:",embed=embed)
                await message.add_reaction(u"\u2705")

            else:
                    await message.author.send("Please complete your profile in #self-roles.")
                    await message.add_reaction(u"\U0001F6AB")
                    
        if message.content.lower() == PREFIX + "help":
            await message.author.send("""```Thank you for using ShinySugar bot, the Dating AI Bot.
-----------------------------
ss!help - To show this message.
ss!profile - To show your profile.
ss!match - To get matched.
-----------------------------
Easy to use ^^```""")
            await message.add_reaction(u"\u2705")
                        

client = MatchingBot()

client.run(TOKEN)
