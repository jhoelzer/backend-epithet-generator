__author__ = "jhoelzer"

from flask import Flask, jsonify
from dotenv import load_dotenv
from backend_epithet_generator.helpers import EpithetGenerator, Vocabulary
from random import randint
import os

app = Flask(__name__)


@app.route("/")
def generate_epithets():
    result = EpithetGenerator().generate_one()
    return jsonify({"epithets": result})


@app.route("/vocabulary")
def vocabulary():
    result = Vocabulary.read_json("resources/data.json")
    return jsonify({"vocabulary": result})


@app.route("/epithets/<int:quantity>")
def generate_multiple_epithets(quantity=1):
    result = EpithetGenerator().generate_multi(quantity)
    return jsonify({"epithets": result})


@app.route('/random')
def generate_random_number_epithets():
    random_epithets = EpithetGenerator().quantity(randint(1, 51))
    return jsonify(random_epithets)
