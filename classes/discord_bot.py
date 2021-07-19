# -*- coding utf-8 -*-

import discord
import asyncio
from discord.ext import commands

class DiscordBot(commands.Bot):

    def __init__(self, command_prefix, token, cogs=[]):
        commands.Bot.__init__(self, command_prefix=command_prefix)
        self.token = token
        for cog in cogs:
            self.load_extension(cog)

    def start_bot(self):
        self.run(self.token)
