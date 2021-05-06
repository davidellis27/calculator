#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, flash, redirect
from calculator_db_funcs_postgresql import db_postgresql_connect, db_postgresql_select, \
     db_postgresql_update, db_postgresql_insert
import requests
import json
import urllib.parse


app = Flask(__name__)

db_conn = db_postgresql_connect()


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        return redirect(url_for('form_register'))

    return render_template('index.html')


@app.route('/basic', methods=('GET', 'POST'))
def index_basic():
    if request.method == 'POST':
        return redirect(url_for('form_register'))

    return render_template('index_basic.html')


def html_head():
    html = ""

    html += '<head>'
    html += '   <meta charset="utf-8">'
    html += '   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'
#    html += '   <link rel="stylesheet" href="static/css/style.css">'
    html += '       <link rel="stylesheet" \
                          href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" \
                          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" \
                          crossorigin="anonymous">'
    html += '	<title>Flask Test</title>'

    html += '<style>'
    html += '.divider25'
    html += '{'
    html += '   width: 20px;'
    html += '   height: auto;'
    html += '   display: inline-block;'
    html += '}'
    html += '</style>'
    html += '</head>'

    return html


def html_jquery_popper_bootstrap():
    html = ""

    html += '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" \
                     integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" \
                     crossorigin="anonymous"></script>'
    html += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" \
                     integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" \
                     crossorigin="anonymous"></script>'
    html += '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" \
                     integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" \
                     crossorigin="anonymous"></script>'

    return html


def html_sidebar():
    html = ""

    html += '<div class="col-1">'
    html += '    <nav class ="navbar bg-dark position-fixed">'
    html += '            <table>'
    html += '            <tr><td>'
    html += '            <p>Hello World</p>'
    html += '            </td></tr>'
    html += '            <tr><td>'
    html += '        <ul class ="nav navbar-nav">'
    html += '            <li class ="nav-item">'
    html += '                <a class ="nav-link" href="#"> Home</a>'
    html += '            </li>'
    html += '            <li class ="nav-item">'
    html += '                <a class ="nav-link" href="#"> Home</a>'
    html += '            </li>'
    html += '            <li class ="nav-item">'
    html += '                <a class ="nav-link" href="#"> Services </a>'
    html += '            </li>'
    html += '            <li class ="nav-item">'
    html += '                <a class ="nav-link" href="#"> Contact </a>'
    html += '            </li>'
    html += '            <li class ="nav-item">'
    html += '                <a class ="nav-link" href="#"> Blogs </a>'
    html += '            </li>'
    html += '        </ul>'
    html += '            </table>'
    html += '    </nav>'
    html += '</div>'

    return html


def html_form_equation(name):
    html = ''

    the_sql = "SELECT addition, subtraction, multiplication, division \
                 FROM calculator \
                WHERE user_name = '" + name + "';"

    rows = db_postgresql_select(db_conn, the_sql)

    html += '<p style="font-size: 24px">' + name + '</p>'

    html += '<table class="table">'
    html += '    <thead>'
    html += '        <tr>'
    html += '        <th style="text-align: center">Add</th>'
    html += '        <th style="text-align: center">Sub</th>'
    html += '        <th style="text-align: center">Mult</th>'
    html += '        <th style="text-align: center">Div</th>'
    html += '        </tr>'
    html += '    </thead>'

    html += '    <tbody>'
    html += '        <tr>'

    for item in rows[0]:
        html += '<td style="text-align: center">' + str(item) + '</td>'

    html += '        </tr>'
    html += '    </tbody>'

    html += '</table>'

    html += '<form method="post">'
    html += '    <div class="row">'
    html += '        <p class="divider25"/>'

    html += '        <div class="form-group">'
    # html += '          <label for="first-number">First Number</label>'
    html += '            <input type="text" name="first_number"'
    html += '                   placeholder="Post title" class="form-control"'
    html += '                   value="First Number"></input>'
    html += '        </div>'

    html += '        <p class="divider25"/>'

    html += '        <div>'
    # html += '          <label for="operation">Choose an operation:</label>'
    html += '            <select name="operation" id="operation" style="font-size: 24px">'
    html += '                <option value="+">+</option>'
    html += '                <option value="-">-</option>'
    html += '                <option value="*">x</option>'
    html += '                <option value="/">/</option>'
    html += '            </select>'
    html += '        </div>'

    html += '        <p class="divider25"/>'

    html += '        <div class="form-group">'
    # html += '          <label for="second_number">Second Number</label>'
    html += '            <input type="text" name="second_number"'
    html += '                   placeholder="Post title" class="form-control"'
    html += '                   value="Second Number"></input>'
    html += '        </div>'
    html += '        <p class="divider25"/>'
    html += '        <p style="font-size: 24px">= ?</p>'
    html += '    </div>'

    html += '    <div class="row">'
    html += '        <p class="divider25"/>'
    html += '        <div class="form-group">'
    html += '            <button type="submit" class="btn btn-primary">Submit</button>'
    html += '        </div>'
    html += '    </div>'
    html += '</form>'

    return html


@app.route('/equation/<name>', methods=('GET', 'POST'))
def form_equation(name):

    if request.method == 'POST':
        number_1 = request.form['first_number']
        number_2 = request.form['second_number']
        operation = request.form['operation']

        the_params = {}
        for variable in ["number_1", "number_2", "operation"]:
            the_params[variable] = eval(variable)

        # urllib.parse.urlencode(the_params)

        print('in form equation')
        print(' the params')
        print(the_params)

        endpoint = 'http://localhost:5000/calculator/v1/calculator_operation'
        response = requests.get(url=endpoint, params=the_params)

        print(' the response')
        print(response.json())

    # else it is GET
    html = ""
    html += '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += html_head()
    html += '<body>'
    html += '   <div class="col-9">'
    html += '       <div class="container">'
    html += '    	<h1>Calculator</h1>'
    html += html_form_equation(name)
    html += '       </div>'
    html += '    </div>'
    html += html_jquery_popper_bootstrap()
    html += '</body>'
    html += '</html>'

    return html


def html_form_new_name(name):
    html = ""

    html += '<form method="post">'
    html += '    <div class="form-group">'

    html += '        <p>I\'ve not seen "' + name + '" before.</p>'
    html += '        <p>You Can:</p>'

    html += '<div class="row">'
    html += '    <p class="divider25"/>'

    html += '    <div class="form-group">'
    html += '        <button type="submit" name="button_1" value="go_on" class="btn btn-primary">Continue</button>'
    html += '    </div>'
    html += '           <p style="margin-left: 1em; padding-top: .5em"> as "' + name + '"</p>'
    html += '    </div>'

    html += '<div class="row">'
    html += '    <p class="divider25"/>'

    html += '    <div class="form-group">'
    html += '        <button type="submit" name="button_1" value="re_enter" class="btn btn-primary">Re-Enter</button>'
    html += '    </div>'
    html += '           <p style="margin-left: 1em; padding-top: .5em">your name</p>'
    html += '    </div>'

    html += '    </div>'
    html += '</form>'

    return html


@app.route('/new_name/<name>', methods=('GET', 'POST'))
def form_new_name(name):

    if request.method == 'POST':
        btn_return = request.form['button_1']

        if btn_return == "re_enter":
            return redirect(url_for('form_register'))

        if btn_return == "go_on":
            the_sql = "INSERT INTO Calculator (user_name, addition, subtraction, multiplication, division) \
                       VALUES ('" + name + "', 0, 0, 0, 0);"
            rows = db_postgresql_insert(db_conn, the_sql)

            if rows:
                return redirect(url_for('form_equation', name=name))
            else:
                pass
                # BATT redirect to an error screen

    html = ""
    html += '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += html_head()
    html += '<body>'
    html += '   <div class="col-4">'
    html += '       <div class="container">'
    html += '    	<h1>Calculator</h1>'
    html += html_form_new_name(name)
    html += '       </div>'
    html += '    </div>'
    html += html_jquery_popper_bootstrap()
    html += '</body>'
    html += '</html>'

    return html


def html_form_register():
    html = ""

    html += '<form method="post">'
    html += '    <div class="form-group">'
    html += '        <label for="register_name">Enter Name</label>'
    html += '        <input type="text" name="register_name"'
    html += '               placeholder="Name" class="form-control"'
    html += '               value=""></input>'
    html += '    </div>'
    html += '    <div class="form-group">'
    html += '        <button type="submit" class="btn btn-primary">Submit</button>'
    html += '    </div>'
    html += '</form>'

    return html


@app.route('/register', methods=('GET', 'POST'))
def form_register():

    if request.method == 'POST':
        name = request.form['register_name']

        # the_sql = "SELECT user_name, addition, subtraction, multiplication, division \
        #              FROM calculator \
        #             WHERE user_name = '" + name + "';"

        the_params = {'name': name}

        # urllib.parse.urlencode(the_params)

        print('In form_register')
        print(' the params')
        print(the_params)

        endpoint = 'http://localhost:5000/calculator/v1/select_user_info'
        response = requests.get(url=endpoint, params=the_params)

        print(' the response')
        print(response)
        print(response.status_code)
        print(response.json())

        #BATT look at return code instead of rows below.  based on first parameter, go to new name or equation.

        if not rows:
            return redirect(url_for('form_new_name', name=name))

        return redirect(url_for('form_equation', name=name))

    html = ""
    html += '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += html_head()
    html += '<body>'
    html += '   <div class="col-4">'
    html += '       <div class="container">'
    html += '    	<h1>Calculator</h1>'
    html += html_form_register()
    html += '       </div>'
    html += '    </div>'
    html += html_jquery_popper_bootstrap()
    html += '</body>'
    html += '</html>'

    return html


if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
