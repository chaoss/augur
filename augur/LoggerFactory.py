import logging
from collections import namedtuple
from augur.logging import AugurLogConfigurer
import LogHandlerFactory
import AugurLogger

HandlerTags = namedtuple("HandlerTags", "info error debug")

class LoggerFactory:
    @staticmethod
    def create_logger(general_tags: str, handler_tags: HandlerTags, author: Author, augur_config, verbose: bool = False,
                      debug: bool = False,
                      ) -> AugurLogger:
        # Get the log directory folder name and append a slash
        logfile_directory = AugurLogConfigurer.get_log_directories(augur_config, reset_logfiles=False) + "/"
        # create new AugurLogger
        logger = AugurLogger()
        # instantiate a log handler Factory
        logHandlerFactory = LogHandlerFactory(general_tags, logfile_directory, author, verbose)
        # attach handlers
        logger.addHandler(logHandlerFactory.create_handler(handler_tags.info, logging.INFO))
        logger.addHandler(logHandlerFactory.create_handler(handler_tags.error, logging.ERROR))
        if debug:
            logger.addHandler(logHandlerFactory.create_handler(handler_tags.debug, logging.DEBUG))
        return logger
