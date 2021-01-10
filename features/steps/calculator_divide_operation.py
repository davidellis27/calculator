from behave import when
from calculator import divide


@when('I input {a} and {b} to calculator to divide')
def step_impl(context, a, b):
    print(u'Step When I input {} and {} to calculator to divide.'. format(a, b))
    context.result = divide(a, b)
    print(u'Stored division result {} in context.'. format(context.result))
