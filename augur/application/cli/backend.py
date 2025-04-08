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

from keyman.KeyClient import KeyPublisher

logger = AugurLogger("augur", reset_logfiles=True).get_logger()


@click.group('server', short_help='Commands for controlling the backend API server & data collection workers')
@click.pass_context
def cli(ctx):
    ctx.obj = DatabaseContext()

@cli.command("start")
@click.option("--disable-collection", is_flag=True, default=False, help="Turns off data collection workers")
@click.option("--development", is_flag=True, default=False, help="Enable development mode, implies --disable-collection")
@click.option("--pidfile", default="main.pid", help="File to store the controlling process ID in")
@click.option('--port')
@test_connection
@test_db_connection
@with_database
@click.pass_context
def start(ctx, disable_collection, development, pidfile, port):
    """Start the Augur server with all configured workers"""
    if development:
        disable_collection = True

    # Start the server
    start_server(port)

    # Start workers if collection is enabled
    if not disable_collection:
        start_workers()

def start_workers():
    """Start the worker processes"""
    worker_processes = determine_worker_processes(0.8, 8)  # 80% of available memory, max 8 processes
    if worker_processes:
        start_celery_worker_processes(worker_processes)

def determine_worker_processes(ratio, maximum):
    """Determine number of worker processes based on available memory"""
    available_memory = psutil.virtual_memory().available
    process_memory = 500 * 1024 * 1024  # 500MB per process
    num_processes = min(int(available_memory * ratio / process_memory), maximum)
    return max(1, num_processes)  # At least 1 process

def start_celery_worker_processes(num_processes, disable_collection=False):
    """Start celery worker processes"""
    if disable_collection:
        return

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
    """Stop the Augur server and workers gracefully"""
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

def start_server(port):
    """Start the server"""
    with open(pidfile, "w") as pidfile_io:
        pidfile_io.write(str(os.getpid()))
        
    try:
        if os.environ.get('AUGUR_DOCKER_DEPLOY') != "1":
            raise_open_file_limit(100000)
    except Exception as e: 
        logger.error(
                    ''.join(traceback.format_exception(None, e, e.__traceback__)))
        
        logger.error("Failed to raise open file limit!")
        raise e
    
    os.environ["AUGUR_PIDFILE"] = pidfile

    try:
        gunicorn_location = os.getcwd() + "/augur/api/gunicorn_conf.py"
    except FileNotFoundError:
        logger.error("\n\nPlease run augur commands in the root directory\n\n")

    host = get_value("Server", "host")

    if not port:
        port = get_value("Server", "port")
    
    os.environ["AUGUR_PORT"] = str(port)
    
    gunicorn_command = f"gunicorn -c {gunicorn_location} -b {host}:{port} augur.api.server:app --log-file gunicorn.log"
    server = subprocess.Popen(gunicorn_command.split(" "))

    logger.info("awaiting Gunicorn start")
    while not server.poll():
        try:
            api_response = requests.get(f"http://{host}:{port}/api")
        except requests.exceptions.ConnectionError as e:
            time.sleep(0.5)
            continue
        
        if not api_response.ok:
            logger.critical("Gunicorn failed to start or was not reachable. Exiting")
            exit(247)
        break
    else:
        logger.critical("Gunicorn was shut down abnormally. Exiting")
        exit(247)
    
    logger.info('Gunicorn webserver started...')
    logger.info(f'Augur is running at: {"http" if development else "https"}://{host}:{port}')
    logger.info(f"The API is available at '{api_response.json()['route']}'")

    if os.path.exists("celerybeat-schedule.db"):
            logger.info("Deleting old task schedule")
            os.remove("celerybeat-schedule.db")

    log_level = get_value("Logging", "log_level")
    celery_beat_process = None
    celery_command = f"celery -A augur.tasks.init.celery_app.celery_app beat -l {log_level.lower()}"
    celery_beat_process = subprocess.Popen(celery_command.split(" "))    
    keypub = KeyPublisher()
    
    if not disable_collection:
        orchestrator = subprocess.Popen("python keyman/Orchestrator.py".split())

        # Wait for orchestrator startup
        if not keypub.wait(republish=True):
            logger.critical("Key orchestrator did not respond in time")
            return
        
        # load keys
        ghkeyman = GithubApiKeyHandler(logger, session)
        glkeyman = GitlabApiKeyHandler(logger)

        for key in ghkeyman.keys:
            keypub.publish(key, "github_rest")
            keypub.publish(key, "github_graphql")

        for key in glkeyman.keys:
            keypub.publish(key, "gitlab_rest")
        
        with DatabaseSession(logger, engine=ctx.obj.engine) as session:

            clean_collection_status(session)
            assign_orphan_repos_to_default_user(session)
        
        create_collection_status_records.si().apply_async()
        time.sleep(3)

        #put contributor breadth back in. Not sure why it was commented out
        contributor_breadth_model.si().apply_async()

        # start cloning repos when augur starts
        clone_repos.si().apply_async()

        augur_collection_monitor.si().apply_async()
        
    else:
        logger.info("Collection disabled")
    
    try:
        server.wait()
    except KeyboardInterrupt:
        
        if server:
            logger.info("Shutting down server")
            server.terminate()

        logger.info("Shutting down all celery worker processes")
        for p in process_list:
            if p:
                p.terminate()

        if celery_beat_process:
            logger.info("Shutting down celery beat process")
            celery_beat_process.terminate()

        if not disable_collection:

            try:
                keypub.shutdown()
                cleanup_collection_status_and_rabbit(logger, ctx.obj.engine)
            except RedisConnectionError:
                pass
            
    os.unlink(pidfile)

def clear_redis_caches():
    """Clears the redis databases that celery and redis use."""

    logger.info("Flushing all redis databases this instance was using")
    celery_purge_command = "celery -A augur.tasks.init.celery_app.celery_app purge -f"
    subprocess.call(celery_purge_command.split(" "))
    redis_connection.flushdb()

def clear_all_message_queues(connection_string):
    queues = ['celery','secondary','scheduling','facade']

    virtual_host_string = connection_string.split("/")[-1]

    #Parse username and password with urllib
    parsed = urlparse(connection_string)

    for q in queues:
        curl_cmd = f"curl -i -u {parsed.username}:{parsed.password} -XDELETE http://localhost:15672/api/queues/{virtual_host_string}/{q}"
        subprocess.call(curl_cmd.split(" "),stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def clear_rabbitmq_messages(connection_string):
    #virtual_host_string = connection_string.split("/")[-1]

    logger.info("Clearing all messages from celery queue in rabbitmq")
    from augur.tasks.init.celery_app import celery_app
    celery_app.control.purge()

    clear_all_message_queues(connection_string)
    #rabbitmq_purge_command = f"sudo rabbitmqctl purge_queue celery -p {virtual_host_string}"
    #subprocess.call(rabbitmq_purge_command.split(" "))

#Make sure that database reflects collection status when processes are killed/stopped.
def clean_collection_status(session):
    session.execute_sql(s.sql.text("""
        UPDATE augur_operations.collection_status 
        SET core_status='Pending',core_task_id = NULL
        WHERE core_status='Collecting' AND core_data_last_collected IS NULL;

        UPDATE augur_operations.collection_status
        SET core_status='Success',core_task_id = NULL
        WHERE core_status='Collecting' AND core_data_last_collected IS NOT NULL;

        UPDATE augur_operations.collection_status 
        SET secondary_status='Pending',secondary_task_id = NULL
        WHERE secondary_status='Collecting' AND secondary_data_last_collected IS NULL;

        UPDATE augur_operations.collection_status 
        SET secondary_status='Success',secondary_task_id = NULL
        WHERE secondary_status='Collecting' AND secondary_data_last_collected IS NOT NULL;

        UPDATE augur_operations.collection_status 
        SET facade_status='Update', facade_task_id=NULL
        WHERE facade_status LIKE '%Collecting%' and facade_data_last_collected IS NULL;

        UPDATE augur_operations.collection_status 
        SET facade_status='Success', facade_task_id=NULL
        WHERE facade_status LIKE '%Collecting%' and facade_data_last_collected IS NOT NULL;

        UPDATE augur_operations.collection_status
        SET facade_status='Pending', facade_task_id=NULL
        WHERE facade_status='Failed Clone' OR facade_status='Initializing';
    """))
    #TODO: write timestamp for currently running repos.

def assign_orphan_repos_to_default_user(session):
    query = s.sql.text("""
        SELECT repo_id FROM repo WHERE repo_id NOT IN (SELECT repo_id FROM augur_operations.user_repos)
    """)

    repos = session.execute_sql(query).fetchall()

    for repo in repos:
        UserRepo.insert(session, repo[0],1)


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
    augur_app.database.execute(s.sql.text("""
        UPDATE augur_operations.collection_status 
        SET core_status='Pending',core_task_id = NULL, core_data_last_collected = NULL;

        UPDATE augur_operations.collection_status 
        SET secondary_status='Pending',secondary_task_id = NULL, secondary_data_last_collected = NULL;

        UPDATE augur_operations.collection_status 
        SET facade_status='Pending', facade_task_id=NULL, facade_data_last_collected = NULL;

        TRUNCATE augur_data.commits CASCADE;
        """))

    logger.info("Repos successfully reset")

@cli.command('processes')
def processes():
    """
    Outputs the name/PID of all Augur server & worker processes"""
    augur_processes = get_augur_processes()
    for process in augur_processes:
        logger.info(f"Found process {process.pid} [{process.name()}] -> Parent: {process.parent().pid}")

def get_augur_processes():
    augur_processes = []
    for process in psutil.process_iter(['cmdline', 'name', 'environ']):
        if process.info['cmdline'] is not None and process.info['environ'] is not None:
            try:
                if os.getenv('VIRTUAL_ENV') in process.info['environ']['VIRTUAL_ENV'] and 'python' in ''.join(process.info['cmdline'][:]).lower():
                    if process.pid != os.getpid():
                        augur_processes.append(process)
            except (KeyError, FileNotFoundError):
                pass
    return augur_processes

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
