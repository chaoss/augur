from pickle import NONE
import pytest
import os
from collections import namedtuple
from augur.LogHandlerFactory import LogHandlerFactory 
# import augur.LoggerFactory
# import augur.LogHandlerFactory
# from augur.LoggerFactory import LoggerFactory
from augur.logging import AugurLogConfigurer
# import augur.AugurLogger
import logging.config



Author = namedtuple("Author", "worker_type port")
HandlerTags = namedtuple("HandlerTags", "info error debug")

temp_dir = os.path.join(os.getcwd(), "util")
config_path = os.path.join(temp_dir, "test.config.json")

def test_handler_exists():
    new = tuple(["first", "last"])
    
    test_handler = LogHandlerFactory("None",'/test_file.txt',Author)
    if test_handler == None:
        print("Handler not created, value is NULL")
    else:
        pass    

def test_handler_args():    
    test_handler = LogHandlerFactory("",'/test_file.txt',Author)

    try:
        test_handler.log_tags
    except ValueError:
        print("Tags not unitialized./n") 
    
    try:
        test_handler.logfile_dir
    except ValueError:
        print("File not unitialized./n") 

    try:
        test_handler.author
    except ValueError:
        print("Author not unitialized./n") 

def test_create_handler():
    handler_test = LogHandlerFactory("None",temp_dir,Author)
    result = handler_test.create_handler("tags",1)
    try:
        result != None
    except:
        "Factory creation failed, result is NULL"

def test_create_debug():
    result = LogHandlerFactory._create_debug_handler 
    try:   
        result != None
    except ValueError:
        "Debug Handler failed, value is NULL"

def test_create_info():
        result = LogHandlerFactory._create_info_handler
        try:
                result != None
        except ValueError:
                "Info Handler failed, value is NULL"

def test_create_error():
        result = LogHandlerFactory._create_error_handler
        try:
                result != None
        except ValueError:
                "Error Handler failed, value is NULL"

# def test_LoggerFactory():
#     factory = LoggerFactory.create_logger(HandlerTags, Author, temp_dir)

#     try:
#         factory != None
#     except ValueError:
#         "Factory failed to initialize"

def test_init_ALC():
    alc = AugurLogConfigurer()
    try:
        alc != None
    except ValueError:
        "Log configuration failed"

def test_disable_log():
    alc = AugurLogConfigurer()
    alc._disable_all_logging()

    try:
        for logger in ["augur", "augur.application", "augur.housekeeper", "augur.config", "augur.cli", "root"]:
            lg = logging.getLogger(logger)
            lg.disabled == False
    except ValueError:
        "Logging not properly disabled" 

def test_config_cli_log():
    alc = AugurLogConfigurer()
    
    test_config = alc.logfile_config
    try:
        test_config != NONE
    except ValueError:
        "Logfiles not properly configured"



