# This bot allows you to use your newly created model to make some really funny as if they were a certain person.
# Requires an already trained model. (run generate_model.ipynb on Google Colab)
# Requires discord.py (or any fork)
import os
import gpt_2_simple as gpt2
from discord.ext import commands

client = commands.Bot(command_prefix="hey sadie ")  # replace this prefix if you want your ai bot to be accurate
sess = None


@client.command()
async def conditional(ctx, length: int, amount: int, *, start):
    msg = await ctx.send("Thinking...\nPlease wait.")
    result = gpt2.generate(sess, truncate="<|endoftext|>", length=length, nsamples=amount, prefix=start,
                           temperature=1, return_as_list=True)
    await msg.delete()
    for n, sample in enumerate(result, start=1):
        await ctx.send(f"SAMPLE {n} - {start}...\n{sample}")

        
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Please use integers, you dumbass.")
        
        
@client.event
async def on_connect():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"
    global sess
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)        

    
@client.event
async def on_ready():
    print("Ready")

client.run("TOKEN")
