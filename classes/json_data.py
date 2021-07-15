import json

class JsonData:
    def __init__(self, filename):
        self.json_filename = filename
        json_file = open(filename, "r")
        self.json_obj = json.load(json_file)
        json_file.close()

    def update_data(self, key, value):
        self.json_obj[key] = value

    def update_file(self):
        json_file = open(self.json_filename, "w")
        json.dump(self.json_obj, json_file)
        json_file.close()
