# To read messages you have to send a message as the bot, that will read all new messages sent between the last message you sent and your new message

import discord
import json

from discord.ext import commands

with open("config.json") as f:
    config = json.load(f)

TOKEN = config.get("TOKEN")
PREFIX = config.get("PREFIX")
channel = ""

GREEN = "\033[92m"
ENDCOLOR = "\033[0m"

client = discord.Client()
bot = commands.Bot(command_prefix=PREFIX, help_command=None, case_insensitive=False)

# Load extension to listen for messages and print
bot.load_extension("cogs.listener")

# Get channel id for the channel the messages gets sent to
@bot.command()
async def makeconnection(ctx):
    msg = await ctx.send("Making connection...")
    channel = ctx.message.channel.id
    send_channel =  bot.get_channel(channel)
    await ctx.send("connection was successfully created")
    while True:
        msg = input("{}<< Message: {}".format(GREEN, ENDCOLOR))
        if msg == "":
            continue
        else:
            await send_channel.send(msg)

bot.run(TOKEN)