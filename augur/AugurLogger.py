import logging

#add additional tags to log messages
class AugurLogger(logging.Logger):

     def info_with_tags (self, additional_tags, message, *args, **kwargs): 
        Logger.debug(self, message, args, kwargs + {"ExtraTags": additional_tags})

     def error_with_tags (self, additional_tags, message, *args, **kwargs): 
        Logger.debug(self, message, args, kwargs + {"ExtraTags": additional_tags})
        
     def debug_with_tags (self, additional_tags, message, *args, **kwargs): 
        Logger.debug(self, message, args, kwargs + {"ExtraTags": additional_tags})
        



    
    
