import logging
from collections import namedtuple
from augur.logging import AugurLogConfigurer

Author = namedtuple("Author", "worker_type port")


class LogHandlerFactory:
    def __int__(self, log_tags: str, logfile_dir: str, author: Author, verbose: bool = False):
        self.log_tags = log_tags
        self.logfile_dir = logfile_dir
        self.author = author
        self.verbose = verbose

    def create_handler(self, handler_tags: str, log_level: int) -> logging.Handler:
        filename = f"{self.logfile_dir}{self.author.worker_type}_{self.author.port}_collection"
        if logging.WARNING == log_level:
            result = self._create_error_handler(filename)
            handler_format = AugurLogConfigurer.error_format_string
        else:
            if logging.DEBUG == log_level:
                result = self._create_debug_handler()
            else:
                result = self._create_info_handler(filename)

            if self.verbose:
                handler_format = AugurLogConfigurer.verbose_format_string
            else:
                handler_format = AugurLogConfigurer.simple_format_string

        result.setLevel(log_level)
        result.setFormatter(handler_format.format(handler_tags=self.log_tags + handler_tags))
        return result

    @staticmethod
    def _create_debug_handler() -> logging.Handler:
        return logging.StreamHandler()

    @staticmethod
    def _create_info_handler(filename: str) -> logging.Handler:
        filename += ".log"
        return logging.FileHandler(filename=filename)

    @staticmethod
    def _create_error_handler(filename: str) -> logging.Handler:
        filename += ".err"
        return logging.FileHandler(filename=filename)
