# -*- coding utf-8 -*-

import json

class JsonData:
    def __init__(self, filename):
        self.json_filename = filename
        json_file = open(filename, "r")
        self.json_obj = json.load(json_file)
        json_file.close()

    def update_data(self, key1, key2, value):
        if key2:
            self.json_obj[key1][key2] = value
        else:
            self.json_obj[key1] = value

    def update_file(self):
        json_file = open(self.json_filename, "w")
        json.dump(self.json_obj, json_file)
        json_file.close()
