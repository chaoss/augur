import click
import os
import sys
from augur.runtime import pass_application
from augur.util import logger
from augur.server import Server
import gunicorn.app.base
from gunicorn.six import iteritems
from gunicorn.arbiter import Arbiter
import multiprocessing as mp
from augur.housekeeper.housekeeper import Housekeeper
import sched
import os
import time
import sys
import atexit
import click
import subprocess

@click.command('run')
@pass_application
def cli(app):

    def get_process_id(name):
        """Return process ids found by name or command
        """
        child = subprocess.Popen(['pgrep', '-f', name], stdout=subprocess.PIPE, shell=False)
        response = child.communicate()[0]
        return [int(pid) for pid in response.split()]

    mp.set_start_method('forkserver', force=True)
    app.schedule_updates()
    master = None

    manager = None
    broker = None
    housekeeper = None
    
    logger.info("Booting broker and its manager...")
    manager = mp.Manager()
    broker = manager.dict()
        
    logger.info("Booting housekeeper...")
    jobs = app.read_config('Housekeeper', 'jobs', 'AUGUR_JOBS', [])
    housekeeper = Housekeeper(
            jobs,
            broker,
            broker_port=app.read_config('Server', 'port', 'AUGUR_PORT', '5000'),
            user=app.read_config('Database', 'user', 'AUGUR_DB_USER', 'root'),
            password=app.read_config('Database', 'password', 'AUGUR_DB_PASS', 'password'),
            host=app.read_config('Database', 'host', 'AUGUR_DB_HOST', '127.0.0.1'),
            port=app.read_config('Database', 'port', 'AUGUR_DB_PORT', '3306'),
            dbname=app.read_config('Database', 'database', 'AUGUR_DB_NAME', 'msr14')
        )

    controller = app.read_config('Workers')
    worker_pids = []
    worker_processes = []
    if controller:
        for worker in controller.keys():
            if controller[worker]['switch']:
                pids = get_process_id("/bin/sh -c cd workers/{} && {}_start".format(worker, worker))
                worker_pids += pids
                if len(pids) > 0:
                    worker_pids.append(pids[0] + 1)
                    pids.append(pids[0] + 1)
                    logger.info("Found and preparing to kill previous {} worker pids: {}".format(worker,pids))
                    for pid in pids:
                        try:
                            os.kill(pid, 9)
                        except:
                            logger.info("Worker process {} already killed".format(pid))
                worker_process = mp.Process(target=worker_start, kwargs={'worker_name': worker}, daemon=True)
                worker_process.start()
                worker_processes.append(worker_process)
                time.sleep(2.5)

    @atexit.register
    def exit():
        try:
            for pid in worker_pids:
                os.kill(pid, 9)
        except:
            logger.info("Worker process {} already killed".format(pid))
        for process in worker_processes:
            logger.info("Shutting down worker process with pid: {} ...".format(process))
            process.terminate()

        if master is not None:
            master.halt()
        logger.info("Shutting down app updates...")
        app.shutdown_updates()
        logger.info("Finalizing config...")
        app.finalize_config()
        logger.info("Shutting down housekeeper updates...")
        if housekeeper is not None:
            housekeeper.shutdown_updates()
    
        # if hasattr(manager, "shutdown"):
            # wait for the spawner and the worker threads to go down
            # 
        if manager is not None:
            manager.shutdown()
            # check if it is still alive and kill it if necessary
            # if manager._process.is_alive():
            manager._process.terminate()
        
        # Prevent multiprocessing's atexit from conflicting with gunicorn
        # logger.info("killing self: {}".format(os.getpid()))
        # os.kill(os.getpid(), 9)
        # os._exit(0)

    host = app.read_config('Server', 'host', 'AUGUR_HOST', '0.0.0.0')
    port = app.read_config('Server', 'port', 'AUGUR_PORT', '5000')
    workers = int(app.read_config('Server', 'workers', 'AUGUR_WORKERS', mp.cpu_count()))
    options = {
        'bind': '%s:%s' % (host, port),
        'workers': workers,
        'accesslog': '-',
        'access_log_format': '%(h)s - %(t)s - %(r)s',
    }
    logger.info('Starting server...')
    master = Arbiter(AugurGunicornApp(options, manager=manager, broker=broker, housekeeper=housekeeper)).run()

def worker_start(worker_name=None):
    logger.info("Booting {}".format(worker_name))
    process = subprocess.Popen("cd workers/{} && {}_start".format(worker_name,worker_name), shell=True)

class AugurGunicornApp(gunicorn.app.base.BaseApplication):
    """
    Loads configurations, initializes Gunicorn, loads server
    """

    def __init__(self, options=None, manager=None, broker=None, housekeeper=None):
        self.options = options or {}
        self.manager = manager
        self.broker = broker
        self.housekeeper = housekeeper
        super(AugurGunicornApp, self).__init__()
        # self.cfg.pre_request.set(pre_request)

    def load_config(self):
        """
        Sets the values for configurations
        """
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        """
        Returns the loaded server
        """
        server = Server(manager=self.manager, broker=self.broker, housekeeper=self.housekeeper)
        return server.app

