# -*- coding utf-8 -*-

from classes.json_data import JsonData
import twitter

class Twitter:
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.api = twitter.Api(
                        consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token_key,
                        access_token_secret=access_token_secret)

        self.json_data = JsonData("json/twitter.json")

    def get_tweet_urls(self, request, command=''):
        if not request:
            return []

        statuses = []
        terms = self.json_data.json_obj[request]
        for term in terms.keys():
            results = self.api.GetSearch(term=f"{term} {command}", since_id=terms[term], count=100)
            if results:
                self.json_data.update_data(request, term, results[0].id)
                statuses += results
        
        self.json_data.update_file()
        
        if not statuses:
            return []
        
        statuses.sort(key=lambda x:x.id)
        urls = []
        for status in statuses:
            urls.append((status.user.screen_name, f"https://twitter.com/{status.user.screen_name}/status/{status.id_str}"))

        return urls
