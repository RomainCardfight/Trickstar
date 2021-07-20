# -*- coding utf-8 -*-

from classes.json_data import JsonData

class Channels(JsonData):
    def __init__(self):
        JsonData.__init__(self, "json/channels.json")

    def get_channel_ids(self, section):
        return self.json_obj[section].values()
