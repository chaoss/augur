import logging
#How to Include AugurLogger?

class LoggerFactory:
    @staticmethod
    def create_logger(handler_tags: str, author: (str, str)) -> AugurLogger:
        #create new AugurLogger
        logger = AugurLogger()
        #attach handlers
        logger.addHandler(LoggerFactory.create_handler(handler_tags, logging.INFO))
        logger.addHandler(LoggerFactory.create_handler(handler_tags, logging.ERROR))
        logger.addHandler(LoggerFactory.create_handler(handler_tags, logging.DEBUG)) # how to determine whether to add debug or not?
        return logger
