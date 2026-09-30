from django.test import Client


def before_scenario(context, scenario):
    context.test = type('TestHelper', (), {})()
    context.test.client = Client()
