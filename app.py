__author__ = "jhoelzer"

from flask import Flask, jsonify
from dotenv import load_dotenv
from backend_epithet_generator.helpers import EpithetGenerator, Vocabulary

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
