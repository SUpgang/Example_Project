"""Main module within the package"""

import time

from .subpackage.submodule1 import say_hello
from .logger.mylogger import get_my_logger

logger = get_my_logger(__name__)


def say_bye():
    """Printing and returning hello"""
    text = "Bye from module"
    logger.info(text)  # replace with logger
    return text


if __name__ == "__main__":

    print("Module started")

    print(say_hello())
    print(say_bye())
    time.sleep(3)

    print("Module ended")
