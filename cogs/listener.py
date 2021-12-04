import discord
from discord.ext import commands

BLUE = "\033[94m"
ENDCOLOR = "\033[0m"

class Listen(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            pass
        else:
            print("{}>> [{}] | Message:{} {}".format(BLUE, message.author, ENDCOLOR, message.content))


def setup(bot):
    bot.add_cog(Listen(bot))