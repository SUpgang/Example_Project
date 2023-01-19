from mypackage.core.coremodule import say_huhu


def test_say_huhu():
    assert say_huhu() == "Huhu!"
