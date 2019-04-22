__author__ = 'jhoelzer'

from flask import Flask, jsonify
from .helpers import EpithetGenerator, Vocabulary
import random

app = Flask(__name__)


@app.route('/')
def generate_epithets():
    e = EpithetGenerator()
    result = e.one_random()
    return jsonify(result)


@app.route('/vocabulary')
def vocabulary():
    v = Vocabulary()
    result = v.read_json('resources/data.json')
    return jsonify(result)


@app.route('/epithets/<int:quantity>')
def generate_multiple_epithets(quantity):
    e = EpithetGenerator()
    result = e.multi_random(quantity)
    return jsonify(result)


@app.route('/random')
def generate_random_number_epithets():
    e = EpithetGenerator()
    random_num = random.randint(1, 51)
    result = e.multi_random(random_num)
    return jsonify(result)
