#!/usr/bin/env python3

import flask
from flask import request, jsonify
from calculator import add, subtract, multiply, divide
from decimal import Decimal


operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
              }

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/calculator', methods=['GET'])
def home():
    return "<h1>Connected to Calculator.</p>"


@app.route('/calculator/v1/calculator_add', methods=['GET'])
def api_add():
    number_1 = Decimal(request.args['number_1'])
    number_2 = Decimal(request.args['number_2'])

    answer = operations['+'](number_1, number_2)

    return jsonify(str(answer))


@app.route('/calculator/v1/calculator_sub', methods=['GET'])
def api_sub():
    number_1 = Decimal(request.args['number_1'])
    number_2 = Decimal(request.args['number_2'])

    return jsonify(str(operations['-'](number_1, number_2)))


@app.route('/calculator/v1/calculator_mult', methods=['GET'])
def api_mult():
    number_1 = Decimal(request.args['number_1'])
    number_2 = Decimal(request.args['number_2'])

    return jsonify(str(operations['*'](number_1, number_2)))


@app.route('/calculator/v1/calculator_div', methods=['GET'])
def api_div():
    number_1 = Decimal(request.args['number_1'])
    number_2 = Decimal(request.args['number_2'])

    return jsonify(str(operations['/'](number_1, number_2)))


app.run()
