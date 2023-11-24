"""Contains examples for how to use some of the features recommended elsewhere."""

import configparser

from loguru import logger


def example_configparser():
    logger.info("Logging just works with loguru!")

    config = configparser.ConfigParser()
    # Read the config file into the config object, pass it the path of the config file.
    config.read("config.ini")
