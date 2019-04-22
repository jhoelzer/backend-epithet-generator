#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This is in Python3
"""

__author__ = 'jhoelzer'

from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def generate_epithets():
    epithets = {'epithets': []}
    return jsonify(epithets)


@app.route('/vocabulary')
def vocabulary():
    vocabulary = {'vocabulary': {}}
    return jsonify(vocabulary)
