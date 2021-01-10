from behave import when
from calculator import add
import requests
from decimal import Decimal
import json


@when('I input {number1} and {number2} to calculator CLI to add')
def step_impl(context, number1, number2):
    print(u'Step When I input {} and {} to calculator to add.'.format(number1, number2))

    context.result = add(number1, number2)
    print(u'Stored addition result {} in context.'.format(context.result))


@when('I pass {url} and {the_params} to calculator API to add')
def step_impl(context, url, the_params):
    the_json_params = json.loads(the_params)
    response = requests.get(url, params=the_json_params)
    print(u'Step When I pass {} and {} to calculator API to add', url, the_json_params)

    if response.status_code != 200:
        raise Exception("Calculator API is not available.")

    context.result = Decimal(response.json())
    print(u'Stored addition result {} in context.'.format(context.result))
