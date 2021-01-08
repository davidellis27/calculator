from behave import given, when, then

@given('Calculator app is run')
def step_impl(context):
    print (u'Step: Given Calculator app is run.')

@then('I get result {out}')
def step_impl(context, out):
    if (context.result == int(out)):
        print(u'Step: Then I get correct result {}, {}.'. format(context.result, out))
        #pass
    else:
        raise Exception("Incorrect result is returned.")
