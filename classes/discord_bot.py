# -*- coding utf-8 -*-

import discord
import asyncio
from discord.ext import commands
from classes.channels import Channels
from classes.twitter import Twitter

class DiscordBot(commands.Bot):

    def __init__(self, token, command_prefix='!', twitter=None, channels=None, cogs=[]):
        commands.Bot.__init__(self, command_prefix=command_prefix)
        self.token = token
        self.twitter = twitter
        self.channels = channels
        for cog in cogs:
            self.load_extension(cog)

    def start_bot(self):
        self.run(self.token)
