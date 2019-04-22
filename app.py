__author__ = "jhoelzer"

from flask import Flask, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


@app.route("/")
def generate_epithets():
    epithets = {"epithets": []}
    return jsonify(epithets)


@app.route("/vocabulary")
def vocabulary():
    vocabulary = {"vocabulary": {}}
    return jsonify(vocabulary)
