# Use this bot to generate a dataset of any Discord user's messages.
# Hint: The more messages you have, the more accurate the AI will be.
# This script uses a bot user instead of a selfbot to reduce the chances of a Discord ban.
# Requires discord.py (or any fork)

# stdlib
import os

# discord.py
import discord
from discord.ext import commands

# third-party
from dotenv import load_dotenv

client = commands.Bot(command_prefix="++")
load_dotenv()


@client.command()
async def fetch(ctx, uid: int, gpt=""):
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
        res = "\n".join(message.content for message in messages)
        name = "dataset.txt"
    else:
        res = "\n".join(f"<|startoftext|> {message.content} <|endoftext|>" for message in messages)
        name = "gpt_dataset.txt"
    with open(name, "w", encoding="utf-8") as f:
        f.write(res)
    await msg.delete()
    await ctx.send(file=discord.File("messages.txt"))


@client.event
async def on_ready():
    print("Ready")

client.run(os.environ.get("TOKEN"))
