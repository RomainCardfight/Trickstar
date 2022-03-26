# -*- coding utf-8 -*-

from discord.ext import commands
import asyncio
import discord
import aiocron
import time
from classes.json_data import JsonData
from classes.channels import Channels
from classes.twitter import Twitter

class Tweets(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        @aiocron.crontab("*/10 * * * *")
        async def send_tweets():
            terms = self.bot.twitter.get_json()
            for term in terms.keys():
                channel_ids = self.bot.channels.get_channel_ids(term)
                tweets = self.bot.twitter.get_tweet_urls(term, ' exclude:retweets')
                for user, url in tweets:
                    for channel_id in channel_ids:
                        time.sleep(2)
                        channel = self.bot.get_channel(channel_id)
                        await channel.send(f"**{user}** tweeted this:\n{url}")

    @commands.command(name='set_channel',
                    description="Setup a channel to post tweets",
                    help='Setup a channel to post tweets (Examples: !set_channel deck, !set_channel vg_en !set_channels vg_jp)')
    @commands.has_permissions(administrator=True)
    async def set_channel(self, ctx, section=None):
        if not section:
            await ctx.send('**Error**: You need to specify an argument (check with !help)')

        elif section not in self.bot.channels.get_keys():
            await ctx.send('**Error**: Unknown value, you need to specify a valid argument (i.e. deck, vg_en or vg_jp)')
        
        else:
            server_id = ctx.message.channel.guild.id
            channel_id = ctx.message.channel.id
            self.bot.channels.update_data(section, str(server_id), channel_id)
            self.bot.channels.update_file()
            await ctx.send(f"**Successfully added this channel to the __{section}__ list!**")

    @commands.command(name='remove_channel',
                    description= 'Remove channel from list',
                    help='Remove channel from list (Examples: !remove_channel deck)')
    @commands.has_permissions(administrator=True)
    async def remove_channel(self, ctx, section=None):
        if not section:
            await ctx.send('**Error**: You need to specify an argument (check with !help)')

        if section not in self.bot.channels.get_keys():
            await ctx.send('**Error**: Unknown value, you need to specify a valid argument (i.e. deck, vg_en or vg_jp)')
        else:
            server_id = ctx.message.channel.guild.id
            self.bot.channels.remove_data(section, str(server_id))
            self.bot.channels.update_file()
            await ctx.send(f"**Successfully removed this channel from the __{section}__ list!**")

def setup(bot):
    bot.add_cog(Tweets(bot))
