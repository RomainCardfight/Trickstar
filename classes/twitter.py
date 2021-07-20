# -*- coding utf-8 -*-

from classes.json_data import JsonData
import twitter

class Twitter(JsonData):
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        JsonData.__init__(self, "json/twitter.json")
        self.api = twitter.Api(
                        consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token_key,
                        access_token_secret=access_token_secret)

    def get_url(self, status):
        return f"https://twitter.com/{status.user.screen_name}/status/{status.id_str}"

    def get_tweet_urls(self, section, command=''):
        if not section:
            return []

        statuses = []
        terms = self.get_section(section)
        for term in terms.keys():
            results = self.api.GetSearch(term=f"{term} {command}", since_id=terms[term], count=100)
            if results:
                self.update_data(section, term, results[0].id)
                statuses += results
                self.update_file()
        
        if not statuses:
            return []
        
        statuses.sort(key=lambda x:x.id)
        urls = []
        for status in statuses:
            urls.append((status.user.screen_name, self.get_url(status)))

        return urls
