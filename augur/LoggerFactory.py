import logging
from augur.logging import AugurLogConfigurer
import LogHandlerFactory
import AugurLogger

class LoggerFactory:
    @staticmethod
    def create_logger(handler_tags: str, logfile_dir: str, author: (str, str), augur_config) -> AugurLogger:
        #Get the log directory folder name and append a slash
        logfile_directory = AugurLogConfigurer.get_log_directories(augur_config, reset_logfiles=False) + "/"
        #create new AugurLogger
        logger = AugurLogger()
        #instantiate a log handler Factory
        logHandlerFactory = LogHandlerFactory(handler_tags, logfile_directory, author)
        #attach handlers
        logger.addHandler(logHandlerFactory.create_handler(handler_tags, logging.INFO))
        logger.addHandler(logHandlerFactory.create_handler(handler_tags, logging.ERROR))
        logger.addHandler(logHandlerFactory.create_handler(handler_tags, logging.DEBUG)) # how to determine whether to add debug or not?
        return logger
