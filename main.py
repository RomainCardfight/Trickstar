# -*- coding utf-8 -*-

from classes.twitter import Twitter
from classes.json_data import JsonData

consumer_key='zs4lO2B7HlnGlkYBTvNvQyxFJ'
consumer_secret='seDbV2XXkIFcqnNXKW5jPXSpD5PLGkCj7JR5PjYcQSZ9mYuqlT'
access_token_key='782185223039619072-pWhcmEVa6NvBz0T4wAf0CfaGRdGhT7s'
access_token_secret='WCsZdhjipgZe5qpTrg4ecnVkcVij4GczxvoYKO9We3YDG'

if __name__ == "__main__":
    twitter = Twitter(consumer_key, consumer_secret, access_token_key, access_token_secret)
    json_data = JsonData("json/twitter.json")
    terms = json_data.json_obj["vg_en_terms"]
    print(twitter.get_tweets(terms))
