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
async def fetch(ctx, user: discord.Member, gpt=""):
    if gpt and gpt != "gpt":
        return await ctx.send(f"Usage: {ctx.prefix}fetch <user> [gpt]\n<> is required, [] is optional")
    if os.path.isfile("dataset.txt"):
        os.remove("dataset.txt")
    if os.path.isfile("gpt_dataset.txt"):
        os.remove("gpt_dataset.txt")
    msg = await ctx.send("Fetching messages...\nThis will take a while.")
    count = 0
    name = None
    for channel in [channel for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]:
        try:
            async for message in channel.history(limit=None):
                count += 1
                print(f"Processed {count} messages")
                if message.author.id == user.id:
                    if not gpt:
                        name = "dataset.txt"
                        with open(name, "a", encoding="utf-8") as f:
                            f.write(f"{message.content}\n")
                    else:
                        name = "gpt_dataset.txt"
                        with open(name, "a", encoding="utf-8") as f:
                            f.write(f"<|startoftext|> {message.content} <|endoftext|>\n")
        except discord.Forbidden:
            pass
    await msg.delete()
    await ctx.send(file=discord.File(name))



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Please provide a valid user.")


@client.event
async def on_ready():
    print("Ready")

client.run(os.environ.get("TOKEN"))
