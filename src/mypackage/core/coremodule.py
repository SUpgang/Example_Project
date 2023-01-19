""" Test """

from ..uipackage.uimodule import say_hello
from .anothermodule import say_bye


def say_huhu():
    return "Huhu!"


def call_hello():
    print(say_hello(), say_bye(), say_huhu())
