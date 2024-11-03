"""Script outside of package to test imports """

import time

# from mypackage.subpackage.submodule1 import say_hello
# from mypackage.module1 import say_bye

from mylogger import get_logger

logger = get_logger(__name__, "./logging.cfg")

if __name__ == "__main__":

    print("Script started")

    logger.info("bla")
    logger.error("test")
    logger.info("test2")
    # print(say_hello())
    # print(say_bye())
    time.sleep(3)

    print("Script ended.")
