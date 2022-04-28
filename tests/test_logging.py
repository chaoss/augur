import click
import os
from os import walk
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
		test_handler
	except:
		print("Handler not created")

def test_handler_args():	
	tag = "test"
	level = 1
	author = ("first", "last")
 
	assert !tag.isEmpty()
	assert level.is_integer()
	assert type(author) is tuple

	test_handler1 = create_handler(tag, level, author)	
