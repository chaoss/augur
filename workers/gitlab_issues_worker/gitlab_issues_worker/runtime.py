from flask import Flask, jsonify, request, Response
import click, os, json, requests, logging
from gitlab_issues_worker.worker import GitLabIssueWorker
from workers.util import read_config, create_server

@click.command()
@click.option('--augur-url', default='http://localhost:5000/', help='Augur URL')
@click.option('--host', default='localhost', help='Host')
@click.option('--port', default=51237, help='Port')
def main(augur_url, host, port):
    """ Declares singular worker and creates the server and flask app that it will be running on
    """
    app = Flask(__name__)

    #load credentials
    broker_host = read_config("Server", "host", "AUGUR_HOST", "0.0.0.0")
    broker_port = read_config("Server", "port", "AUGUR_PORT", 5000)
    database_host = read_config('Database', 'host', 'AUGUR_DB_HOST', 'host')
    worker_info = read_config('Workers', 'gitlab_issues_worker', None, None)

    worker_port = worker_info['port'] if 'port' in worker_info else port

    while True:
        try:
            r = requests.get("http://{}:{}/AUGWOP/heartbeat".format(host, worker_port)).json()
            if 'status' in r:
                if r['status'] == 'alive':
                    worker_port += 1
        except:
            break

    logging.basicConfig(filename='worker_{}.log'.format(worker_port), filemode='w', level=logging.INFO)

    config = { 
            'id': 'com.augurlabs.core.gitlab_issues_worker.{}'.format(worker_port),
            'location': 'http://{}:{}'.format(read_config('Server', 'host', 'AUGUR_HOST', 'localhost'),worker_port),
            "key": read_config("Database", "gitlab_api_key", "AUGUR_GITLAB_API_KEY", "gitlab_api_key"),
            "password": read_config('Database', 'password', 'AUGUR_DB_PASSWORD', 'password'),
            "port": read_config('Database', 'port', 'AUGUR_DB_PORT', 'port'),
            "user": read_config('Database', 'user', 'AUGUR_DB_USER', 'user'),
            "database": read_config('Database', 'name', 'AUGUR_DB_NAME', 'database'),
            "endpoint": "https://bestpractices.coreinfrastructure.org/projects.json",
            "display_name": "",
            "description": "",
            "required": 1,
            "type": "string"
        }

    #create instance of the worker
    app.worker = GitLabIssueWorker(config) # declares the worker that will be running on this server with specified config

    create_server(app, None)
    logging.info("Starting Flask App with pid: " + str(os.getpid()) + "...")
    app.run(debug=app.debug, host=host, port=worker_port)

    if app.worker._child is not None:
        app.worker._child.terminate()
        
    try:
        requests.post('http://{}:{}/api/unstable/workers/remove'.format(server['host'],server['port']), json={"id": config['id']})
    except:
        pass

    logging.info("Killing Flask App: " + str(os.getpid()))
    os.kill(os.getpid(), 9)



