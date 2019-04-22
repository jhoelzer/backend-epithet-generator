import random
import json


class Vocabulary:
    def read_json(path, mode='r'):
        # resources/data.json
        with open(path, mode=mode) as handle:
            return json.load(handle)


class EpithetGenerator:
    def generate_one(self):
        data = Vocabulary.read_json("resources/data.json")
        return "{} {} {}".format(random.choice(data["Column 1"]),
                                  random.choice(data["Column 2"]),
                                  random.choice(data["Column 3"]))

    def generate_multi(self, quantity):
        multi_epithets_list = []
        for _ in range(quantity):
            multi_epithets_list.append(self.generate_one())
        return multi_epithets_list
