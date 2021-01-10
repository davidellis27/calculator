from behave import when
from calculator import divide
import requests
from decimal import Decimal
import json


@when('I input {a} and {b} to calculator to divide')
def step_impl(context, a, b):
    print(u'Step When I input {} and {} to calculator to divide.'. format(a, b))
    context.result = divide(a, b)
    print(u'Stored division result {} in context.'. format(context.result))


@when('I pass {url} and {the_params} to calculator API to divide')
def step_impl(context, url, the_params):
    the_json_params = json.loads(the_params)
    response = requests.get(url, params=the_json_params)
    print(u'Step When I pass {} and {} to calculator API to divide', url, the_json_params)

    if response.status_code != 200:
        raise Exception("Calculator API is not available.")

    context.result = Decimal(response.json())
    print(u'Stored division result {} in context.'.format(context.result))
