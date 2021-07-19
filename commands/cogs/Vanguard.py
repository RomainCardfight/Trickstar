from discord.ext import commands
import asyncio
import discord

class Vanguard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test')
    async def hello(self, ctx):
        await ctx.send('Hello!')

def setup(bot):
    bot.add_cog(Vanguard(bot))
