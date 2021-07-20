# -*- coding utf-8 -*-

from classes.twitter import Twitter
from classes.json_data import JsonData
from classes.discord_bot import DiscordBot
from classes.channels import Channels
from tokens.tokens import consumer_key, consumer_secret
from tokens.tokens import access_token_key, access_token_secret, bot_token

if __name__ == "__main__":
    twitter = Twitter(consumer_key, consumer_secret, access_token_key, access_token_secret)
    channels = Channels()
    bot = DiscordBot(bot_token, '!', twitter, channels, ["commands.cogs.Tweets"])
    bot.start_bot()
