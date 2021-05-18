import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("connected")

@bot.command()
async def hello(ctx):
    nick = ctx.message.author #.mention #.id
    await ctx.send(f"ну привет {nick}")

    await ctx.author.send(f"и отдельное куку {nick}")

bot.run(str(os.environ.get('BOT_TOKEN')))

