#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        return redirect(url_for('register'))

    return render_template('index.html')


@app.route('/basic', methods=('GET', 'POST'))
def index_basic():
    if request.method == 'POST':
        return redirect(url_for('register'))

    return render_template('index_basic.html')


def html_head():
    html = ""

    html += '<head>'
    html += '   <meta charset="utf-8">'
    html += '   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'
    html += '   <link rel="stylesheet" href="static/css/style.css">'
    html += '       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">'
    html += '	<title>Flask Test</title>'
    html += '</head>'

    return html


def html_jquery_popper_bootstrap():
    html = ""

    html += '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>'
    html += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>'
    html += '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>'

    return html


def html_form_insert_1(title, content):
    html = ""

    html += '<form method="post">'
    html += '    <div class="form-group">'
    html += '<table class="table">'
    html += '<tr>'
    html += '<td>'
    html += '        <label for="title">Title</label>'
    html += '</td>'
    html += '<td>'
    html += '        <input type="text" name="title"'
    html += '               placeholder="Post title" class="form-control"'
    html += '               value="' + title + '"></input>'
    html += '</td>'
    html += '</tr>'

    html += '<td>'
    html += '        <label for="content">Content</label>'
    html += '</td>'
    html += '<td>'
    html += '        <textarea name="content" placeholder="Post content"'
    html += '                  class="form-control">' + content + '</textarea>'
    html += '</td>'
    html += '</tr>'
    html += '</table>'
    html += '    </div>'

    html += '    <div class="form-group">'
    html += '        <button type="submit" class="btn btn-primary">Submit</button>'
    html += '    </div>'
    html += '</form>'

    return html


def html_form_insert(title, content):
    html = ""

    html += '<form method="post">'
    html += '    <div class="form-group">'
    html += '        <label for="title">Title</label>'
    html += '        <input type="text" name="title"'
    html += '               placeholder="Post title" class="form-control"'
    html += '               value="' + title + '"></input>'
    html += '    </div>'

    html += '    <div class="form-group">'
    html += '        <label for="content">Content</label>'
    html += '        <textarea name="content" placeholder="Post content"'
    html += '                  class="form-control">' + content + '</textarea>'
    html += '    </div>'
    html += '    <div class="form-group">'
    html += '        <button type="submit" class="btn btn-primary">Submit</button>'
    html += '    </div>'
    html += '</form>'

    return html


def html_wrapper_row_start():
    html = ""

    html += '<div class="row">'

    return html


def html_wrapper_row_end():
    html = ""

    html += '</div>'

    return html


def html_sidebar_old():
    html = ""

    html += '<div class="col-1">'
    html += '    <nav class ="navbar bg-light position-fixed">'
    html += '    Title<br>'
    html += '    Title<br>'
    html += '    Title<br>'
    html += '    Title<br>'
    html += '    </nav>'
    html += '</div>'

    return html


def html_sidebar():
    html = ""

    html += '<div class="col-1">'
    html += '    <nav class ="navbar bg-dark position-fixed">'
    #    html += '        <p class -"navbar-text">Title</p>'
    #    html += '<div class="container-fluid">'
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
    #    html += '</div>'
    html += '    </nav>'
    html += '</div>'

    return html


@app.route('/insert', methods=('GET', 'POST'))
def form_insert():
    title = 'Start title'
    content = 'Start content'

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

    html = ""
    html += '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += html_head()
    html += '<body>'
    html += html_wrapper_row_start()
    html += html_sidebar()
    html += '   <div class="col-6">'
    html += '       <div class="container">'
    html += '    	<h1>Welcome to Blah</h1>'
    html += '           <p>' + title + '</p>'
    html += '           <p>' + content + '</p>'
    html += html_form_insert_1(title, content)
    html += '       </div>'
    html += '   </div>'
    html += html_wrapper_row_end()
    html += html_jquery_popper_bootstrap()
    html += '</body>'
    html += '</html>'

    return html


if __name__ == '__main__':
    app.run()
