# -*- coding utf-8 -*-

from classes.json_data import JsonData
import twitter

class Twitter:
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.api = twitter.Api(
                        consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token_key,
                        access_token_secret=access_token_secret
                    )
        self.json_data = JsonData("json/twitter.json")

    def get_tweet_urls(self, term):
        statuses = self.api.GetSearch(term=term, count=100)
        urls = []
        for s in statuses:
            urls.append(f"https://twitter.com/{s.user.screen_name}/status/{s.id_str}")
        return urls

    def get_tweets(self, terms, command=''):
        urls = []
        for term in terms:
            urls += self.get_tweet_urls(term + command)
        return urls
