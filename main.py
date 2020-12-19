import discord
from discord.ext import commands
import random

TOKEN = "NzEyODc5NDkxNTY3MDU5MDI4.XsX-ww.hBUZbNt_L5wgVmlp5EphKeIPZJI"

client = commands.AutoShardedBot(command_prefix="$")
client.remove_command('help')
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

@client.command()
async def help(ctx):
    await ctx.channel.send("I am Death Roll Bot built by Smirf123, I can't do much now but I will get more features soon")
@client.command()
async def roll(ctx):
   val = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
   cchoice = 3
   while(cchoice>1):
       cchoice = random.choice(val)
       if cchoice > 1:
           emb=discord.Embed(title=f"You got {cchoice}")
           emb.add_field(name="Roll again", value="Type any message to continue")
           await ctx.send(embed=emb)
           [cchoice for cchoice in val if cchoice>cchoice]
           def check(m):
               return m.author==ctx.author
           await client.wait_for('message', timeout=45.0, check=check)
       elif cchoice == 1:
           embed=discord.Embed(title="You Lost")
           embed.add_field(name="You got 1 on this roll", value="Try again with $roll")
           await ctx.send(embed=embed)
           break


client.run(TOKEN)