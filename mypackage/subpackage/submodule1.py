""" Submodule example """

from ..logger.mylogger import get_my_logger

logger = get_my_logger(__name__)


def say_hello():
    """Printing and returning hello"""
    text = "Hello from submodule1"
    logger.info(text)
    return text
