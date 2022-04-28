import click
import os
import json
import pandas as pd
import tempfile
import logging
import logging.config
import logging.handlers
import LogHandlerFactory
import atexit
import shutil
import coloredlogs
from logging import FileHandler, StreamHandler, Formatter
from multiprocessing import Process, Queue, Event, current_process
from time import sleep
from pathlib import Path
from copy import deepcopy
from augur.cli import pass_logs_dir
from queue import Queue
from workers.util import read_config
from workers.worker_base import Worker
from workers.worker_git_integration import WorkerGitInterfaceable
from augur.config import AugurConfig, default_config
from augur import ROOT_AUGUR_DIRECTORY

temp_dir = os.path.join(os.getcwd(), "util")
config_path = os.path.join(temp_dir, "test.config.json")

def test_handler_exists():
	try:
		test_handler = create_handler("test", 1, ("first", "last"))
		test_handler != None
	except:
		print("Handler not created, value is NULL")

def test_handler_args():	
	tag = "test"
	level = 1
	author = ("first", "last")
 
	assert !tag.isEmpty()
	assert level.is_integer()
	assert type(author) is tuple

	test_handler1 = create_handler(tag, level, author)

def test_LHF_exists():
	Author = namedtuple("Author", "worker_type port")
	
	try:
		LHF = LogHandlerFactory.__init__("tags", "dir",Author, False)
		LHF != None
	except:
		print("LogHandlerFactory was not initialized")

def test_create_handler():
	
	try:
		result = LogHandlerFactory.create_handler("tags",1)
		result != None
	except:
		"Factory creation failed, result is NULL"

def test_create_debug():
	try:
		result = LogHandlerFactory._create_debug_handler	
		result != None
	except:
		"Debug Handler failed, value is NULL"

def test_create_info():
        try:
                result = LogHandlerFactory._create_info_handler
                result != None
        except:
                "Info Handler failed, value is NULL"

def test_create_error():
        try:
                result = LogHandlerFactory._create_error_handler
                result != None
        except:
                "Error Handler failed, value is NULL"

##def test_log_query():

##def test_log_format():

##def log_location():

##def test_workers_log():
