""" Submodule example """

from mylogger import get_logger

logger = get_logger(__name__, "./logging.cfg")


def say_hello():
    """Printing and returning hello"""
    text = "Hello from submodule1"
    logger.info(text)
    return text
