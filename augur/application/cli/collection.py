#SPDX-License-Identifier: MIT
"""
Augur library commands for controlling the data collection workers
"""
import os
import click
import logging
import psutil
import signal
import uuid
import traceback
import requests
from redis.exceptions import ConnectionError as RedisConnectionError
from urllib.parse import urlparse

from augur.tasks.start_tasks import augur_collection_monitor, create_collection_status_records
from augur.tasks.git.facade_tasks import clone_repos
from augur.tasks.github.util.github_api_key_handler import GithubApiKeyHandler
from augur.tasks.gitlab.gitlab_api_key_handler import GitlabApiKeyHandler
from augur.tasks.data_analysis.contributor_breadth_worker.contributor_breadth_worker import contributor_breadth_model
from augur.tasks.init.redis_connection import redis_connection 
from augur.application.db.models import UserRepo
from augur.application.db.session import DatabaseSession
from augur.application.logs import AugurLogger
from augur.application.db.lib import get_value
from augur.application.cli import test_connection, test_db_connection, with_database, DatabaseContext
import sqlalchemy as s

logger = AugurLogger("augur", reset_logfiles=True).get_logger()

@click.group('collection', short_help='Commands for controlling the data collection workers')
@click.pass_context
def cli(ctx):
    ctx.obj = DatabaseContext()

@cli.command("start")
@click.option("--disable-collection", is_flag=True, default=False, help="Turns off data collection workers")
@click.option("--development", is_flag=True, default=False, help="Enable development mode, implies --disable-collection")
@click.option("--pidfile", default="collection.pid", help="File to store the controlling process ID in")
@test_connection
@test_db_connection
@with_database
@click.pass_context
def start(ctx, disable_collection, development, pidfile):
    """Start the collection workers"""
    if development:
        disable_collection = True

    # Start workers if collection is enabled
    if not disable_collection:
        start_workers(pidfile)

def start_workers(pidfile):
    """Start the worker processes"""
    worker_processes = determine_worker_processes(0.8, 8)  # 80% of available memory, max 8 processes
    if worker_processes:
        start_celery_worker_processes(worker_processes, pidfile)

def determine_worker_processes(ratio, maximum):
    """Determine number of worker processes based on available memory"""
    available_memory = psutil.virtual_memory().available
    process_memory = 500 * 1024 * 1024  # 500MB per process
    num_processes = min(int(available_memory * ratio / process_memory), maximum)
    return max(1, num_processes)  # At least 1 process

def start_celery_worker_processes(num_processes, pidfile, disable_collection=False):
    """Start celery worker processes"""
    if disable_collection:
        return

    with open(pidfile, "w") as pidfile_io:
        pidfile_io.write(str(os.getpid()))

    for i in range(num_processes):
        start_worker_process(i)

def start_worker_process(worker_id):
    """Start a single worker process"""
    worker_logger = AugurLogger(f"worker_{worker_id}").get_logger()
    try:
        subprocess.Popen(["celery", "-A", "augur.tasks.init.celery_app", "worker", "-l", "info"])
        worker_logger.info(f"Started worker {worker_id}")
    except Exception as e:
        worker_logger.error(f"Failed to start worker {worker_id}: {str(e)}")

@cli.command('stop')
@test_connection
@test_db_connection
@with_database
@click.pass_context
def stop(ctx):
    """Stop the collection workers gracefully"""
    stop_logger = AugurLogger("stop").get_logger()
    augur_stop(signal.SIGTERM, stop_logger, ctx.obj.engine)

def augur_stop(stop_signal, stop_logger, engine):
    """Stop Augur processes with the given signal"""
    processes = get_augur_processes()
    if processes:
        _broadcast_signal_to_processes(processes, stop_signal, stop_logger)
        cleanup_collection_status_and_rabbit(stop_logger, engine)

def cleanup_collection_status_and_rabbit(cleanup_logger, engine):
    """Clean up collection status and RabbitMQ"""
    with DatabaseSession(logger=cleanup_logger) as session:
        clean_collection_status(session)
    clear_redis_caches()
    clear_all_message_queues(os.getenv("RABBITMQ_CONNECTION_STRING"))

def _broadcast_signal_to_processes(process_list, broadcast_signal=signal.SIGTERM, given_logger=None):
    """Send signal to all processes in the list"""
    if not process_list:
        return

    for proc in process_list:
        try:
            proc.send_signal(broadcast_signal)
            if given_logger:
                given_logger.info(f"Sent signal {broadcast_signal} to process {proc.pid}")
        except psutil.NoSuchProcess:
            if given_logger:
                given_logger.warning(f"Process {proc.pid} no longer exists")
        except Exception as e:
            if given_logger:
                given_logger.error(f"Error sending signal to process {proc.pid}: {str(e)}")
