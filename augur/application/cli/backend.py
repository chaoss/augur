#SPDX-License-Identifier: MIT
"""
Augur library commands for controlling the backend components
"""
import resource
import os
import time
import subprocess
import click
import logging
import psutil
import signal
import sys
from redis.exceptions import ConnectionError as RedisConnectionError
from celery import chain, signature, group
import uuid
import traceback
from sqlalchemy import update


from augur import instance_id
from augur.tasks.start_tasks import augur_collection_monitor, CollectionState
from augur.tasks.init.redis_connection import redis_connection 
from augur.application.db.models import Repo, CollectionStatus
from augur.application.db.session import DatabaseSession
from augur.application.db.util import execute_session_query
from augur.application.logs import AugurLogger
from augur.application.config import AugurConfig
from augur.application.cli import test_connection, test_db_connection 
import sqlalchemy as s
from sqlalchemy import or_, and_


logger = AugurLogger("augur", reset_logfiles=True).get_logger()


def create_collection_status(logger):

    with DatabaseSession(logger) as session:
        query = s.sql.text("""
        SELECT repo_id FROM repo WHERE repo_id NOT IN (SELECT repo_id FROM augur_operations.collection_status)
        """)

        repos = session.execute_sql(query).fetchall()

        for repo in repos:
            CollectionStatus.insert(session,repo[0])


@click.group('server', short_help='Commands for controlling the backend API server & data collection workers')
def cli():
    pass

@cli.command("start")
@click.option("--disable-collection", is_flag=True, default=False, help="Turns off data collection workers")
@click.option("--development", is_flag=True, default=False, help="Enable development mode, implies --disable-collection")
@click.option('--port')
@test_connection
@test_db_connection
def start(disable_collection, development, port):
    """Start Augur's backend server."""

    try:
        if os.environ.get('AUGUR_DOCKER_DEPLOY') != "1":
            raise_open_file_limit(100000)
    except Exception as e: 
        logger.error(
                    ''.join(traceback.format_exception(None, e, e.__traceback__)))
        
        logger.error("Failed to raise open file limit!")
        raise e
    
    if development:
        os.environ["AUGUR_DEV"] = "1"
        logger.info("Starting in development mode")

    try:
        gunicorn_location = os.getcwd() + "/augur/api/gunicorn_conf.py"
    except FileNotFoundError:
        logger.error("\n\nPlease run augur commands in the root directory\n\n")

    db_session = DatabaseSession(logger)
    config = AugurConfig(logger, db_session)
    host = config.get_value("Server", "host")

    if not port:
        port = config.get_value("Server", "port")
        
    db_session.invalidate()

    gunicorn_command = f"gunicorn -c {gunicorn_location} -b {host}:{port} augur.api.server:app"
    server = subprocess.Popen(gunicorn_command.split(" "))

    time.sleep(3)
    logger.info('Gunicorn webserver started...')
    logger.info(f'Augur is running at: http://127.0.0.1:{port}')

    scheduling_worker_process = None
    core_worker_process = None
    secondary_worker_process = None
    celery_beat_process = None
    if not disable_collection:

        if os.path.exists("celerybeat-schedule.db"):
            logger.info("Deleting old task schedule")
            os.remove("celerybeat-schedule.db")

        scheduling_worker = f"celery -A augur.tasks.init.celery_app.celery_app worker -l info --concurrency=1 -n scheduling:{uuid.uuid4().hex}@%h -Q scheduling"
        core_worker = f"celery -A augur.tasks.init.celery_app.celery_app worker -l info --concurrency=14 -n core:{uuid.uuid4().hex}@%h"
        secondary_worker = f"celery -A augur.tasks.init.celery_app.celery_app worker -l info --concurrency=5 -n secondary:{uuid.uuid4().hex}@%h -Q secondary"
        
        scheduling_worker_process = subprocess.Popen(scheduling_worker.split(" "))
        core_worker_process = subprocess.Popen(core_worker.split(" "))
        secondary_worker_process = subprocess.Popen(secondary_worker.split(" "))

        time.sleep(5)

        create_collection_status(logger)
        
        with DatabaseSession(logger) as session:
            clean_collection_status(session)

        augur_collection_monitor.si().apply_async()

        celery_command = "celery -A augur.tasks.init.celery_app.celery_app beat -l debug"
        celery_beat_process = subprocess.Popen(celery_command.split(" "))    

    else:
        logger.info("Collection disabled")   
    
    try:
        server.wait()
    except KeyboardInterrupt:
        
        if server:
            logger.info("Shutting down server")
            server.terminate()

        if core_worker_process:
            logger.info("Shutting down celery process: core")
            core_worker_process.terminate()

        if scheduling_worker_process:
            logger.info("Shutting down celery process: scheduling")
            scheduling_worker_process.terminate()

        if secondary_worker_process:
            logger.info("Shutting down celery process: secondary")
            secondary_worker_process.terminate()

        if celery_beat_process:
            logger.info("Shutting down celery beat process")
            celery_beat_process.terminate()

        try:
            cleanup_after_collection_halt(logger)
        except RedisConnectionError:
            pass


@cli.command('stop')
def stop():
    """
    Sends SIGTERM to all Augur server & worker processes
    """
    logger = logging.getLogger("augur.cli")
    _broadcast_signal_to_processes(given_logger=logger)

    cleanup_after_collection_halt(logger)

@cli.command('kill')
def kill():
    """
    Sends SIGKILL to all Augur server & worker processes
    """
    logger = logging.getLogger("augur.cli")
    _broadcast_signal_to_processes(broadcast_signal=signal.SIGKILL, given_logger=logger)

    cleanup_after_collection_halt(logger)

def cleanup_after_collection_halt(logger):
    clear_redis_caches()
    connection_string = ""
    with DatabaseSession(logger) as session:
        config = AugurConfig(logger, session)
        connection_string = config.get_section("RabbitMQ")['connection_string']

        clean_collection_status(session)

    clear_rabbitmq_messages(connection_string)

def clear_redis_caches():
    """Clears the redis databases that celery and redis use."""

    logger.info("Flushing all redis databases this instance was using")
    celery_purge_command = "celery -A augur.tasks.init.celery_app.celery_app purge -f"
    subprocess.call(celery_purge_command.split(" "))
    redis_connection.flushdb()

def clear_rabbitmq_messages(connection_string):
    virtual_host_string = connection_string.split("/")[-1]

    logger.info("Clearing all messages from celery queue in rabbitmq")
    rabbitmq_purge_command = f"sudo rabbitmqctl purge_queue celery -p {virtual_host_string}"
    subprocess.call(rabbitmq_purge_command.split(" "))

#Make sure that database reflects collection status when processes are killed/stopped.
def clean_collection_status(session):
    session.execute_sql(s.sql.text("""
        UPDATE augur_operations.collection_status 
        SET core_status='Pending'
        WHERE core_status='Collecting';
        UPDATE augur_operations.collection_status 
        SET secondary_status='Pending'
        WHERE secondary_status='Collecting';
        UPDATE augur_operations.collection_status 
        SET facade_status='Update', facade_task_id=NULL
        WHERE facade_status LIKE '%Collecting%';
        UPDATE augur_operations.collection_status
        SET facade_status='Pending'
        WHERE facade_status='Failed Clone';
    """))

@cli.command('export-env')
def export_env(config):
    """
    Exports your GitHub key and database credentials
    """

    export_file = open(os.getenv('AUGUR_EXPORT_FILE', 'augur_export_env.sh'), 'w+')
    export_file.write('#!/bin/bash')
    export_file.write('\n')
    env_file = open(os.getenv('AUGUR_ENV_FILE', 'docker_env.txt'), 'w+')

    for env_var in config.get_env_config().items():
        if "LOG" not in env_var[0]:
            logger.info(f"Exporting {env_var[0]}")
            export_file.write('export ' + env_var[0] + '="' + str(env_var[1]) + '"\n')
            env_file.write(env_var[0] + '=' + str(env_var[1]) + '\n')

    export_file.close()
    env_file.close()

@cli.command('repo-reset')
@test_connection
@test_db_connection
def repo_reset(augur_app):
    """
    Refresh repo collection to force data collection
    """
    augur_app.database.execute(s.sql.text("""UPDATE augur_operations.collection_status 
        SET core_status='Pending';
        UPDATE augur_operations.collection_status 
        SET secondary_status='Pending';
        UPDATE augur_operations.collection_status 
        SET facade_status='Update'
        WHERE facade_status='Collecting' OR facade_status='Success' OR facade_status='Error';
        UPDATE augur_operations.collection_status
        SET facade_status='Pending'
        WHERE facade_status='Failed Clone';
        TRUNCATE augur_data.commits CASCADE;
        """))

    logger.info("Repos successfully reset")

@cli.command('processes')
def processes():
    """
    Outputs the name/PID of all Augur server & worker processes"""
    augur_processes = get_augur_processes()
    for process in augur_processes:
        logger.info(f"Found process {process.pid}")

def get_augur_processes():
    augur_processes = []
    for process in psutil.process_iter(['cmdline', 'name', 'environ']):
        if process.info['cmdline'] is not None and process.info['environ'] is not None:
            try:
                if os.getenv('VIRTUAL_ENV') in process.info['environ']['VIRTUAL_ENV'] and 'python' in ''.join(process.info['cmdline'][:]).lower():
                    if process.pid != os.getpid():
                        augur_processes.append(process)
            except KeyError:
                pass
    return augur_processes

def _broadcast_signal_to_processes(broadcast_signal=signal.SIGTERM, given_logger=None):
    if given_logger is None:
        _logger = logger
    else:
        _logger = given_logger
    augur_processes = get_augur_processes()
    if augur_processes:
        for process in augur_processes:
            if process.pid != os.getpid():
                logger.info(f"Stopping process {process.pid}")
                try:
                    process.send_signal(broadcast_signal)
                except psutil.NoSuchProcess:
                    pass


def raise_open_file_limit(num_files):
    """
    sets number of open files soft limit 
    """
    current_soft, current_hard = resource.getrlimit(resource.RLIMIT_NOFILE)

    # if soft is already greater than the requested amount then don't change it
    if current_soft > num_files:
        return

    # if the requested amount is greater than the hard limit then set the hard limit to the num_files value
    if current_hard <= num_files:
        current_hard = num_files

    resource.setrlimit(resource.RLIMIT_NOFILE, (num_files, current_hard))

    return


def print_repos(repos):

    for index, repo in enumerate(repos):

        repo_git = repo.repo_git
        print(f"\t{index}: {repo_git}")

def remove_repos(repos):

    print("Note: To remove multiple repos at once use the python slice syntax")
    print("For example '0:3' removes repo 0, 1, and 2")

    while True:
        if len(repos) == 1:
            print("Only one repo left returning..")
            return

        print_repos(repos)
        user_input = input("To exit enter: -1. Enter index of repo or slice to remove multiple: ")

        if user_input == "-1":
            break

        if ":" in user_input:
            user_slice = slice(*map(lambda x: int(x.strip()) if x.strip() else None, user_input.split(':')))
            try:
                del repos[user_slice]
            except IndexError:
                print("Invalid input. Please input a number or slice")
                continue

        else: 
            try:
                user_input = int(user_input)
            except ValueError:
                print("Invalid input. Please input a number or slice")
                continue

            try:
                del repos[user_input]
            except IndexError:
                print("Invalid input. Please input a number or slice")
                continue


def order_repos(repos):

    print("\n\nPlease enter a comma indicating the order the repos should be collected")
    print("If you would like to order some of them but randomize the rest just enter the order you would like and the rest will be randomized")
    print("For example with 5 repos '3,4' would collect repo 3, then 4, and then repos 1, 2, and 5 would be randomly ordered")
    print_repos(repos)

    while True:
        user_input = input("Order input: ")        

        # creates a list of indexes in the order that the user wanted
        ordered_index_strings = user_input.split(",")

        try:
            # convert list of strings to integers
            ordered_index_ints = [int(i) for i in ordered_index_strings]
        except ValueError:
            print("Invalid input. Please input a comma separated list indicating the order")
            continue

        invalid_entry = False
        for index in ordered_index_ints:
            try:
                repos[index]
            except IndexError:
                print(f"Invalid entry: {index}. Make sure your input is a comma separated list")
                invalid_entry = True

        if invalid_entry:
            continue

        break

    # adds all the other indexes the user did not specify an order for
    for index in range(0, len(repos)):

        if index in ordered_index_ints:
            continue

        ordered_index_ints.append(index)

    # converts list of indexes into list of repo git urls
    repo_git_urls = [repos[index] for index in ordered_index_ints]

    return repo_git_urls

# def initialize_components(augur_app, disable_housekeeper):
#     master = None
#     manager = None
#     broker = None
#     housekeeper = None
#     worker_processes = []
#     mp.set_start_method('forkserver', force=True)

#     if not disable_housekeeper:

#         manager = mp.Manager()
#         broker = manager.dict()
#         housekeeper = Housekeeper(broker=broker, augur_app=augur_app)

#         controller = augur_app.config.get_section('Workers')
#         for worker in controller.keys():
#             if controller[worker]['switch']:
#                 for i in range(controller[worker]['workers']):
#                     logger.info("Booting {} #{}".format(worker, i + 1))
#                     worker_process = mp.Process(target=worker_start, name=f"{worker}_{i}", kwargs={'worker_name': worker, 'instance_number': i, 'worker_port': controller[worker]['port']}, daemon=True)
#                     worker_processes.append(worker_process)
#                     worker_process.start()

#     augur_app.manager = manager
#     augur_app.broker = broker
#     augur_app.housekeeper = housekeeper

#     atexit._clear()
#     atexit.register(exit, augur_app, worker_processes, master)
#     return AugurGunicornApp(augur_app.gunicorn_options, augur_app=augur_app)

# def worker_start(worker_name=None, instance_number=0, worker_port=None):
#     try:
#         time.sleep(30 * instance_number)
#         destination = subprocess.DEVNULL
#         process = subprocess.Popen("cd workers/{} && {}_start".format(worker_name,worker_name), shell=True, stdout=destination, stderr=subprocess.STDOUT)
#         logger.info("{} #{} booted.".format(worker_name,instance_number+1))
#     except KeyboardInterrupt as e:
#         pass
