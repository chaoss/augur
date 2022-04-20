import logging


class LogHandlerFactory:
    @staticmethod
    def create_handler(handler_tag: str, log_level: int, author: (str, str)) -> logging.Handler:
        return logging.Handler()

    @staticmethod
    def _create_debug_handler() -> logging.Handler:
        return logging.Handler()

    @staticmethod
    def _create_info_handler() -> logging.Handler:
        return logging.Handler()

    @staticmethod
    def _create_error_handler() -> logging.Handler:
        return logging.Handler()
