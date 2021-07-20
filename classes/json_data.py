# -*- coding utf-8 -*-

import json

class JsonData:
    def __init__(self, filename):
        self.json_filename = filename
        json_file = open(filename, "r")
        self.json_obj = json.load(json_file)
        json_file.close()

    def get_json(self):
        return self.json_obj

    def get_section(self, section):
        return self.json_obj[section]

    def get_keys(self):
        return self.json_obj.keys()

    def get_values(self, section):
        return self.json_obj[section].values()

    def update_data(self, key1, key2, value):
        self.json_obj[key1][key2] = value

    def update_file(self):
        json_file = open(self.json_filename, "w")
        json.dump(self.json_obj, json_file, indent=4)
        json_file.close()
