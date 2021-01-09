from behave import given, when, then
from calculator import add

@when('I input {number1} and {number2} to calculator to add')
def step_impl(context, number1, number2):
    print(u'Step When I input {} and {} to calculator to add.'. format(number1, number2))
    context.result = add(number1, number2)
    print(u'Stored addition result {} in context.'. format(context.result))

