""" Proof of concept for GUI App without python installation """

from mypackage.logger.mylogger import get_my_logger
from mypackage.ui.main_window import test_window

logger = get_my_logger(__name__, console_level="debug", file_level="warning")

if __name__ == "__main__":
    logger.debug("Debugtest")
    logger.info("Infotest")
    logger.warning("Warningtest")

    test_window()
