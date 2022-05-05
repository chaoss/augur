from logging import Logger 
import logging
#add additional tags to log messages
class AugurLogger(Logger):

     def info_with_tags (self, additional_tags, message, *args, **kwargs):
        self.info(message, *args, **(kwargs | {"extra": {"ExtraTags": additional_tags}}))

     def error_with_tags (self, additional_tags, message, *args, **kwargs): 
        self.error(message, *args, **(kwargs | {"extra": {"ExtraTags": additional_tags}}))
        
     def debug_with_tags (self, additional_tags, message, *args, **kwargs): 
        self.debug(message, *args, **(kwargs | {"extra": {"ExtraTags": additional_tags}}))

     def warning_with_tags (self, additional_tags, message, *args, **kwargs): 
        self.warning(message, *args, **(kwargs | {"extra": {"ExtraTags": additional_tags}}))

     def critical_with_tags (self, additional_tags, message, *args, **kwargs): 
        self.critical(message, *args, **(kwargs | {"extra": {"ExtraTags": additional_tags}}))
        



    
    
