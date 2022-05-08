from logging import Logger


# add additional tags to log messages
class AugurLogger(Logger):
    def info_with_tags(self, additional_tags, message, *args, **kwargs):
        kwargs.update({"extra": {"ExtraTags": additional_tags}})
        self.info(message, *args, **kwargs)

    def error_with_tags(self, additional_tags, message, *args, **kwargs):
        kwargs.update({"extra": {"ExtraTags": additional_tags}})
        self.error(message, *args, **kwargs)

    def debug_with_tags(self, additional_tags, message, *args, **kwargs):
        kwargs.update({"extra": {"ExtraTags": additional_tags}})
        self.debug(message, *args, **kwargs)

    def warning_with_tags(self, additional_tags, message, *args, **kwargs):
        kwargs.update({"extra": {"ExtraTags": additional_tags}})
        self.warning(message, *args, **kwargs)

    def critical_with_tags(self, additional_tags, message, *args, **kwargs):
        kwargs.update({"extra": {"ExtraTags": additional_tags}})
        self.critical(message, *args, **kwargs)
