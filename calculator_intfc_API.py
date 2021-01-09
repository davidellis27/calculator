#!/usr/bin/env python3

import flask
from flask import request, jsonify
from calculator import add, subtract, multiply, divide

operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
              }

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Connected to Calculator.</p>"


@app.route('/v1/calculator_add', methods=['GET'])
def api_add():
    number_1 = int(request.args['number_1'])
    number_2 = int(request.args['number_2'])

    return jsonify(str(operations['+'](number_1, number_2)))


app.run()
