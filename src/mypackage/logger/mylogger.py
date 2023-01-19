"""Provides a simple logger and the setup methods"""

import os
import logging

from typing import Optional

# Init root logger (once at first import)
root_logger = logging.getLogger("")
root_logger.setLevel(logging.DEBUG)


def get_my_logger(
    name: str,
    console_level: Optional[str] = None,
    file_level: Optional[str] = None,
    file_path: str = "./logs/debug.log",
    format_string: Optional[str] = None,
    date_fmt_string: Optional[str] = None,
):
    """
    Runs the setup to create a python logger.
    Use:
        logger = get_my_logger(__name__)
        logger.info('Test')
    """

    # Overrun default logging levels
    if console_level:
        cns_lvl = convert_level(console_level)
    else:
        cns_lvl = logging.DEBUG

    if file_level:
        fl_lvl = convert_level(file_level)
    else:
        fl_lvl = logging.WARNING

    # Create a new logger
    new_logger = logging.getLogger(name)

    # Set formatter
    if not date_fmt_string:
        date_fmt_string = "%Y/%m/%d %H:%M:%S"
    if not format_string:
        format_string = "[%(asctime)s]    %(name)-15s [%(levelname)-7s]: %(message)s"

    formatter = logging.Formatter(fmt=format_string, datefmt=date_fmt_string)

    # create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(cns_lvl)
    console_handler.setFormatter(formatter)
    new_logger.addHandler(console_handler)

    # create file  handler and set level
    if file_path:
        # Create folder if it does not exist
        check_folder(os.path.dirname(file_path))

        file_handler = logging.FileHandler(file_path)
        file_handler.setLevel(fl_lvl)
        file_handler.setFormatter(formatter)
        new_logger.addHandler(file_handler)

    return new_logger


def check_folder(path: str):
    """Checks if a directory exists otherwise creates it"""
    if not os.path.exists(path):
        os.makedirs(path)


def convert_level(input_level: str):
    """Converts level as string to logging level to avoid import"""
    if isinstance(input_level, str):
        level_clean = input_level.lower()
        if level_clean == "debug":
            return logging.DEBUG
        elif level_clean == "info":
            return logging.INFO
        elif level_clean == "warning":
            return logging.WARNING
        elif level_clean == "error":
            return logging.ERROR
        elif level_clean == "critical":
            return logging.CRITICAL
        else:
            raise ValueError("Logging level not valid.")
    else:
        # In case of logging Level just return it
        return input_level
