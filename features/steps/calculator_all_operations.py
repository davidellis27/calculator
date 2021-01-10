from behave import given, then
import requests


@given('Calculator CLI app is run')
def step_impl(context):
    print(u'Step: Given Calculator CLI app is run.')
    # Should use context to validate app is run


@then('I get result {out}')
def step_impl(context, out):
    if context.result == int(out):
        print(u'Step: Then I get correct result {}, {}.'.format(context.result, out))
        # pass
    else:
        raise Exception("Incorrect result is returned.")


@given('Calculator API is available {url_1}')
def step_impl(context, url_1):
    response = requests.get(url_1)

    print("response code:" + str(response.status_code))

    if response.status_code == 200:
        print(u'Step: Given Calculator API is available.')
    else:
        raise Exception("Calculator API is not available.")
