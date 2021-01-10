from behave import when
from calculator import multiply


@when('I input {a} and {b} to calculator to multiply')
def step_impl(context, a, b):
    print(u'Step When I input {} and {} to calculator to multiply.'. format(a, b))
    context.result = multiply(a, b)
    print(u'Stored multiplication result {} in context.'. format(context.result))
