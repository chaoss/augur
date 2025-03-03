#SPDX-License-Identifier: MIT

"""
Augur library commands for controlling the backend components
"""

import os
import click
import subprocess
import uuid
import time
import logging
import signal as os_signal
import psutil
# from redis.exceptions import ConnectionError as RedisConnectionError

from augur.application.logs import AugurLogger
from augur.application.cli import test_connection, test_db_connection, with_database, DatabaseContext
from augur.application.cli._cli_util import _broadcast_signal_to_processes, raise_open_file_limit, clear_rabbitmq_messages
from augur.application.config_sync import update_db_from_file, update_file_from_db

logger = AugurLogger("augur", reset_logfiles=False).get_logger()

@click.group('tasks', short_help='Commands for controlling the backend tasks process')
@click.pass_context
def cli(ctx):
    ctx.obj = DatabaseContext()

@cli.command("start")
@test_connection
@test_db_connection
def start():
    """Start Augur's celery process."""

    # Update database configuration from file on startup
    logger.info("Updating database configuration from file...")
    if not update_db_from_file():
        logger.warning("Failed to update database configuration from file")

    raise_open_file_limit(100000)

    scheduling_worker_process = None
    core_worker_process = None
    secondary_worker_process = None

    scheduling_worker = f"celery -A augur.tasks.init.celery_app.celery_app worker -l info --concurrency=1 -n scheduling:{uuid.uuid4().hex}@%h -Q scheduling"
    core_worker = f"celery -A augur.tasks.init.celery_app.celery_app worker -l info --concurrency=90 -n core:{uuid.uuid4().hex}@%h"
    secondary_worker = f"celery -A augur.tasks.init.celery_app.celery_app worker -l info --concurrency=20 -n secondary:{uuid.uuid4().hex}@%h -Q secondary"
    
    scheduling_worker_process = subprocess.Popen(scheduling_worker.split(" "))
    core_worker_process = subprocess.Popen(core_worker.split(" "))
    secondary_worker_process = subprocess.Popen(secondary_worker.split(" "))
    time.sleep(5)

    try:
        scheduling_worker_process.wait()
    except KeyboardInterrupt:

        # Update file configuration from database on shutdown
        logger.info("Updating file configuration from database...")
        if not update_file_from_db():
            logger.warning("Failed to update file configuration from database")

        if scheduling_worker_process or core_worker_process or secondary_worker_process:
            logger.info("Shutting down celery process")

        if scheduling_worker_process:
            scheduling_worker_process.terminate()

        if core_worker_process:
            core_worker_process.terminate()

        if secondary_worker_process:
            secondary_worker_process.terminate()

        try:
            clear_rabbitmq_messages()
            
        except Exception as e:
            pass

@cli.command('stop')
@with_database
@click.pass_context
def stop(ctx):
    """
    Sends SIGTERM to all Augur tasks processes
    """
    cli_logger = logging.getLogger("augur.cli")

    # Update file configuration from database on shutdown
    cli_logger.info("Updating file configuration from database...")
    if not update_file_from_db():
        cli_logger.warning("Failed to update file configuration from database")

    augur_stop(os_signal.SIGTERM, cli_logger)

@cli.command('kill')
@with_database
@click.pass_context
def kill(ctx):
    """
    Sends SIGKILL to all Augur tasks processes
    """
    cli_logger = logging.getLogger("augur.cli")

    # Update file configuration from database on shutdown
    cli_logger.info("Updating file configuration from database...")
    if not update_file_from_db():
        cli_logger.warning("Failed to update file configuration from database")

    augur_stop(os_signal.SIGKILL, cli_logger)

@cli.command('processes')
def processes():
    """
    Outputs the name/PID of all Augur tasks process"""
    augur_processes = get_augur_tasks_processes()
    for process in augur_processes:
        logger.info(f"Found process {process.pid}")

def augur_stop(signal_type, cli_logger):
    """
    Stops augur with the given signal, 
    and cleans up the tasks
    """

    augur_processes = get_augur_tasks_processes()
 
    _broadcast_signal_to_processes(augur_processes, logger=cli_logger, broadcast_signal=signal_type)

    cleanup_after_tasks_halt(cli_logger)


def cleanup_after_tasks_halt(cli_logger):
    
    try:
        # Get the connection string and queues for RabbitMQ
        from augur.application.db.lib import get_value
        connection_string = get_value("RabbitMQ", "connection_string")
        queues = ['celery', 'secondary', 'scheduling', 'facade']
        clear_rabbitmq_messages(connection_string, queues, cli_logger)
        
    except Exception as e:
        cli_logger.warning(f"Error clearing RabbitMQ messages: {str(e)}")
        pass

def get_augur_tasks_processes():
    augur_tasks_processes = []
    for process in psutil.process_iter(['cmdline', 'name', 'environ']):
        if process.info['cmdline'] is not None and process.info['environ'] is not None:
            try:
                if is_tasks_process(process):
                    augur_tasks_processes.append(process)
            except (KeyError, FileNotFoundError):
                pass
    return augur_tasks_processes

def is_tasks_process(process):

    command = ''.join(process.info['cmdline'][:]).lower()
    if os.getenv('VIRTUAL_ENV') in process.info['environ']['VIRTUAL_ENV'] and 'python' in command:
                    
        if process.pid != os.getpid():
            
            if ("augur.tasks.init.celery_app.celery_app" in command and "frontend" not in command):
                return True
            
    return False

@cli.command("clear-tasks")
@test_connection
@test_db_connection
def clear():
    while True:
        user_input = str(input("Warning this will remove all the tasks from all instances on this server!\nWould you like to proceed? [y/N]"))

        if not user_input:
            logger.info("Exiting")
            return
        
        if user_input in ("y", "Y", "Yes", "yes"):
            logger.info("Removing all tasks")
            celery_purge_command = "celery -A augur.tasks.init.celery_app.celery_app purge -f"
            subprocess.call(celery_purge_command.split(" "))
            return

        if user_input in ("n", "N", "no", "NO"):
            logger.info("Exiting")
            return
        else:
            logger.error("Invalid input")

    
