# This bot allows you to use your newly created model to make some really funny as if they were a certain person.
# Requires an already trained model. (run generate_model.ipynb on Google Colab)
# Requires discord.py (or any fork)

# stdlib
import os

# discord.py
import discord
from discord.ext import commands

# third-party
from dotenv import load_dotenv
import gpt_2_simple as gpt2

client = commands.Bot(command_prefix="ai ")
load_dotenv()
sess = None


@client.command()
async def conditional(ctx, length: int, amount: int, *, start):
    if length > 250 or amount > 10:
        return await ctx.send("You can only make up to 10 250 character samples.")
    msg = await ctx.send("<a:typing:906926432142389249>\u200b")  # please replace this message
    result = gpt2.generate(sess, truncate="<|endoftext|>", length=length, nsamples=amount, prefix=start,
                           temperature=1, return_as_list=True)
    e = discord.Embed(title="The AI says...", description=f"{start}...", color=discord.Colour.blue())
    e.set_footer(text=f"{amount} samples generated")
    for n, sample in enumerate(result, start=1):
        e.add_field(name=f"SAMPLE {n}", value=sample)
    await msg.edit(content=None, embed=e)

        
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(f"Please use integers.\n{ctx.prefix}conditional [length] [amount] [prefix]")
        
        
@client.event
async def on_connect():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"
    global sess
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)        

    
@client.event
async def on_ready():
    print("Ready")

client.run(os.environ.get("TOKEN"))
