import logging
import sys

import colorlog
from celery.utils.log import get_task_logger


def get_logger():
    if 'celery' in sys.argv[0]:
        task_logger = get_task_logger(__name__)
        return task_logger

    logger = logging.getLogger('Qscan')
    if not logger.handlers:
        init_logger()

    return logging.getLogger('Qscan')


def init_logger():
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        fmt = '%(log_color)s[%(asctime)s] [%(levelname)s] '
              '[%(threadName)s] [%(filename)s:%(lineno)d] %(message)s', datefmt = "%Y-%m-%d %H:%M:%S"))

    logger = colorlog.getLogger('Qscan')

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.propagate = False