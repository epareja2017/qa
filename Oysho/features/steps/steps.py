from behave import *

# This should be added to environments.py
# from steps.actionwords import Actionwords
#
# def before_scenario(context, scenario):
#     context.actionwords = Actionwords.new(nil)

use_step_matcher('re')


@given(r'the user opens "(.*)"')
def impl(context, website = "http://www.google.es"):
    context.actionwords.the_user_opens_website(website)


@when(r'the user searches for "(.*)"')
def impl(context, word = "Hiptest"):
    context.actionwords.the_user_searches_for_word(word)


@then(r'the title should be "(.*)"')
def impl(context, title = "Tecnilógica"):
    context.actionwords.the_title_should_be_title(title)


@given(r'a user that wants to register on "(.*)"')
def impl(context, website = "http://www.oysho.es"):
    context.actionwords.a_user_that_wants_to_register_on_website(website)


@when(r'the user credentials are introduced  "(.*)" "(.*)" "(.*)"')
def impl(context, user_mail = "newuser@gmail.com", birth_date = "10/02/2001", password = "Hola1234"):
    context.actionwords.the_user_credentials_are_introduced(user_mail, birth_date, password)


@then(r'the user is registered')
def impl(context):
    context.actionwords.the_user_is_registered()
