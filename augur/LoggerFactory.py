import logging
from collections import namedtuple
from augur.AugurLogger import AugurLogger
from augur.LogHandlerFactory import LogHandlerFactory, Author

HandlerTags = namedtuple("HandlerTags", "info error debug")


class LoggerFactory:
    @staticmethod
    def create_logger(name: str, general_tags: str, handler_tags: HandlerTags, author: Author,
                      logfile_dir, verbose: bool = False, debug: bool = False) -> AugurLogger:
        # create new AugurLogger
        logger = AugurLogger(name)
        # instantiate a log handler Factory
        log_handler_factory = LogHandlerFactory(general_tags, logfile_dir, author, verbose)
        # attach handlers
        logger.addHandler(log_handler_factory.create_handler(handler_tags.info, logging.INFO))
        logger.addHandler(log_handler_factory.create_handler(handler_tags.error, logging.ERROR))
        if debug:
            logger.addHandler(log_handler_factory.create_handler(handler_tags.debug, logging.DEBUG))
        return logger
