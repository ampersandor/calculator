from functools import wraps
import logging
from inspect import getframeinfo, stack
from enum import Enum

class color(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_logger(file_name):
    """
    Create and configure a logger.

    Args:
        file_name (str): The name of the log file.

    Returns:
        logging.Logger: The configured logger.
    """
    logger = logging.Logger(file_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(f"{file_name.split('.')[0]}.log")
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s]  %(levelname)s  %(message)s")
    color_formatter = logging.Formatter(f"{color.OKGREEN.value}[%(asctime)s]{color.ENDC.value}  {color.OKCYAN.value}%(levelname)s{color.ENDC.value}  %(message)s")
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(color_formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

def my_logger(original_function):
    """
    Decorator to log function calls and results.

    Args:
        original_function: The function to be decorated.

    Returns:
        Function: The decorated function.
    """
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        py_file_caller = getframeinfo(stack()[1][0])
        file_name = py_file_caller.filename.split("/")[-1].split(".")[0]
        code_context = py_file_caller.code_context[0].split("=")[-1].split("(")[0].strip()
        logger = get_logger(file_name)
        logger.info(f'Start "<{code_context}>" Arguments: {args}, kwargs - {kwargs}')
        try:
            res = original_function(*args, **kwargs)
            logger.info(f'End   "<{code_context}>" Returns: {res}')
            return res
        except Exception as e:
            logger.error(f'{e}\n\tfilename: {py_file_caller.filename}\n\tlinenum: {py_file_caller.lineno}\n\tcontext: {py_file_caller.code_context}')
            raise

    return wrapper

