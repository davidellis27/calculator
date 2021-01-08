from behave import given, when, then
from calculator import subtract

@when('I input {a} and {b} to calculator to subtract')
def step_impl(context, a, b):
    print(u'Step When I input {} and {} to calclator subtract.'. format(a, b))
    context.result = subtract(a, b)
    print(u'Stored subtraction result {} in context.'. format(context.result))

