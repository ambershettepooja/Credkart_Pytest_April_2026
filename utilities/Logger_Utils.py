import logging
from venv import logger


class log_generator_class:

    @staticmethod
    def loggen_method():
        log_file = logging.FileHandler(".\\Logs\\CredKart.log")
        log_format = logging.Formatter(" %(asctime)s : %(levelname)s : %(funcName)s : %(lineno)d : %(message)s")
        log_file.setFormatter(log_format)
        logger = logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger



"""
file
format
same update in same file


'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL
"""