import pytest


class TestSayHello:

    # say_hello returns the correct greeting text
    def test_returns_correct_greeting_text(self, mocker):
        from mypackage.subpackage.submodule1 import say_hello

        expected_text = "Hello from submodule1"
        result = say_hello()
        assert result == expected_text

    # logger is not initialized
    def test_logger_not_initialized(self, mocker):
        from mypackage.subpackage.submodule1 import say_hello

        logger_mock = mocker.patch("mypackage.subpackage.submodule1.logger")
        say_hello()
        logger_mock.info.assert_called_once_with("Hello from submodule1")
