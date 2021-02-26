#!/usr/bin/env python3

import dash
import dash_core_components as dcc
import dash_html_components as html

import flask
# import pandas as pd
# import time
import os

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash('app', server=server)


# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

first_chart = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Mares eat oats and does eat oats, but little lambs eat ivy.'''),

    dcc.Graph(
        id='example-graph-1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': u'Thing 1'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Thing 2'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
    ])


app.layout = html.Div([

    html.H1(children='Hello Calculator'),
    html.P(children='''Mares eat oats and does eat oats, but little lambs eat ivy.'''),

    first_chart,

    html.Label(children='Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),

    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5,
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': u'Thing 1'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Thing 2'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

    dcc.Graph(
                figure={
                    "data": [
                        {
                            "x": [1, 2, 3],
                            "y": [4, 1, 2],
                            "type": "lines",
                        },
                    ],
                    "layout": {"title": "Avocados Sold"},
                },
            )

], style={'columnCount': 1})

if __name__ == '__main__':
    app.run_server()
