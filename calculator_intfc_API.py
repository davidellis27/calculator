#!/usr/bin/env python3

import flask
from flask import request, jsonify
from calculator import add, subtract, multiply, divide, operations
from decimal import Decimal
from calculator_db_funcs_postgresql import db_postgresql_connect, db_postgresql_select, \
    db_postgresql_update, db_postgresql_insert

app = flask.Flask(__name__)
app.config["DEBUG"] = True

db_conn = db_postgresql_connect()


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


@app.route('/calculator/v1/calculator_operation', methods=['GET'])
def api_operation():
    number_1 = Decimal(request.args['number_1'])
    number_2 = Decimal(request.args['number_2'])
    operation = request.args['operation']

    return jsonify(str(operations[operation](number_1, number_2)))


@app.route('/calculator/v1/select_user_info', methods=['GET'])
def api_select_user_info():
    name = request.args['name']

    print('in api_select_user_info')
    print(' name')
    print(name)

    the_sql = "SELECT 1, \
                      user_name, \
                      addition, \
                      subtraction, \
                      multiplication, \
                      division \
                 FROM calculator \
                WHERE user_name = '" + name + "';"

    rows = db_postgresql_select(db_conn, the_sql)

    print(' rows')
    print(rows)

    if rows:
        return jsonify(rows)
    else:
        return jsonify("[[0]]")


app.run(host='localhost', port=5000, debug=True)
