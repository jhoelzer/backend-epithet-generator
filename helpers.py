import random
import json


class Vocabulary:
    """
    Handle loading in a JSON file with proper unfinished swears in it!

    Usage:
        data = Vocabulary.read_json("/path/to/data.json")
    """

    def read_json(path, mode='r'):
        with open(path, mode=mode) as handle:
            return json.load(handle)


class EpithetGenerator:
    """
    Handle creating and returning one or more epithets

    Usage:
        result = EpithetGenerator().one_random()
        OR
        result = EpithetGenerator().multi_random(quantity)
    """

    def one_random(self):
        data = Vocabulary.read_json("resources/data.json")
        first_word = random.choice(data["Column 1"])
        second_word = random.choice(data["Column 2"])
        third_word = random.choice(data["Column 3"])
        return "{} {} {}!".format(first_word, second_word, third_word)

    def multi_random(self, quantity):
        multi_epithets_list = []
        for _ in range(quantity):
            multi_epithets_list.append(self.one_random() + "!")
        return multi_epithets_list
