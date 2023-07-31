import logging
from dataclasses import dataclass


def create_logger(name: str, level: int = logging.DEBUG) -> logging.Logger:
    import sys

    logger = logging.Logger(name)
    ch = logging.StreamHandler(sys.stdout)

    formatting = "[{}] %(asctime)s\t%(levelname)s\t%(module)s.%(funcName)s#%(lineno)d | %(message)s".format(
        name
    )
    formatter = logging.Formatter(formatting)
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    logger.setLevel(level)

    return logger


class UnknownServiceaccountToken(Exception):
    pass


@dataclass
class ServiceaccountInfo:
    ca_certificate: str
    namespace: str
    token: str
