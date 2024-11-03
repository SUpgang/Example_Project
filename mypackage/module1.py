"""Main module within the package"""

import time
from mylogger import get_logger

from .subpackage.submodule1 import say_hello

logger = get_logger(__name__, "./logging.cfg")


def say_bye():
    """Printing and returning hello"""
    text = "Bye from module"
    logger.info(text)
    return text


if __name__ == "__main__":

    print("Module started")

    print(say_hello())
    print(say_bye())
    time.sleep(3)

    print("Module ended")
