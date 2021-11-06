# Use this bot to generate a dataset of any Discord user's messages.
# Hint: The more messages you have, the more accurate the AI will be.
# This script uses a bot user instead of a selfbot to reduce the chances of a Discord ban.
# Requires discord.py (or any fork)

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="++")


@client.command()
async def fetch(ctx, uid: int, gpt=""):
    if not ctx.me.guild_permissions.administrator:
        return await ctx.send("I need the `ADMINISTRATOR` permission to fetch!")
    msg = await ctx.send("Fetching messages...\nThis will take a while.")
    messages = []
    count = 0
    for channel in [channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]:
        try:
            async for message in channel.history(limit=None):
                count += 1
                print(f"Processed {count} messages")
                if message.author.id == uid:
                    messages.append(message)
        except discord.Forbidden:
            pass
    if not gpt:
        res = "\n".join([message.content for message in messages])
    else:
        res = "\n".join([f"<|startoftext|> {message.content} <|endoftext|>" for message in messages])
    with open("messages.txt", "w", errors="ignore") as f:
        f.write(res)
    await msg.delete()
    await ctx.send(file=discord.File("messages.txt"))


@client.event
async def on_ready():
    print("Ready")

client.run("TOKEN")
    
