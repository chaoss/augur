#SPDX-License-Identifier: MIT
"""
Creates routes for the broker
"""

import logging
import time
import subprocess
import requests
import json
from flask import request, Response
from operator import itemgetter

logger = logging.getLogger(__name__)

""" Broker dict structure:
{
    'tasks': {
        * model name *: {
            * str value of given list *: {
                'user_queue': [
                    * user defined task *,
                    ...
                ],
                'maintain_queue': [
                    * housekeeper defined task *,
                    ...
                ] #,
                # 'completed': ?????
            },
            ...
        },
        ...
    },
    'workers': {
        * worker name *: {
            'id': * worker name *,
            # 'user_queue': [
            #     * user defined task *,
            #     ...
            # ],
            # 'maintain_queue': [
            #     * housekeeper defined task *,
            #     ...
            # ],
            'status': * worker status (e.g. 'Idle') *,
            'location': * worker location *,
            'given': [
                * type of data this worker is able to accept (aka be "given") *,
                ...
            ],
            'models': [
                * type of data this worker is able to collect *,
                ...
            ]
        }
        ...
    }
}
"""

# TODO: not this...
def worker_start(worker_name=None):
    process = subprocess.Popen("cd workers/{} && {}_start".format(worker_name,worker_name), shell=True)

def process_queues(broker):

    unsorted_queue = []

    for model in list(broker['tasks']._getvalue().keys()):
        for given in list(broker['tasks'][model]._getvalue().keys()):
            unsorted_queue.append({
                'model': model,
                'given': given,
                'user_queue_length': len(broker['tasks'][model][given]['user_queue']),
                'maintain_queue_length': len(broker['tasks'][model][given]['maintain_queue']),
            })
    
    # p queue sorted by maintain queue then user queue (user length highest priority)
    priority_queue = sorted(unsorted_queue, key=itemgetter(
        'user_queue_length', 'maintain_queue_length'), reverse=True)

    for subject in priority_queue:

        # Find idle compatible workers
        compatible_workers = []

        for worker_id in list(broker['workers']._getvalue().keys()):
            worker = broker['workers'][worker_id]
            models = worker['models']
            givens = worker['given']

            if subject['model'] in models and eval(subject['given']) in givens \
                    and worker['status'] == 'Idle':
                compatible_workers.append(worker)

        # send tasks to compatible workers
        compatible_queues_proxy = get_compatible_queues_proxy(server.broker, model, given)
        user_queue = compatible_queues_proxy['user_queue']
        maintain_queue = compatible_queues_proxy['maintain_queue']

        while (user_queue or maintain_queue) and compatible_workers:
            worker_to_accept = compatible_workers.pop(0)
            task_to_send = user_queue.pop(0) if len(user_queue) > 0 else maintain_queue.pop(0)

            # Check if worker is alive
            response = requests.get(f"{worker_proxy['location']}/AUGWOP/heartbeat").json()

            if 'status' not in response:
                logger.error(f"Worker: {worker_id}'s heartbeat did not return a response, setting " +
                    "worker status as 'Disconnected'\n")
                worker_proxy['status'] = 'Disconnected'
                continue

            if response['status'] != 'alive':
                logger.info(f"Worker: {worker_id} is busy.\n")
                continue

            logger.info(f"Worker {worker_to_accept['id']} is idle, preparing to send the " +
                f"{task_to_send['display_name']} task to {worker_proxy['location']}/AUGWOP/task\n")
            try:
                requests.post(f"{worker_proxy['location']}/AUGWOP/task", json=task_to_send)
                worker_to_accept['status'] = "Working"
            except:
                logger.error(f"Sending Worker: {worker_to_accept['id']} a task did not return a response, " +
                    "setting worker status as 'Disconnected'\n")
                worker_proxy['status'] = "Disconnected"
                # If the worker died, then restart it
                worker_start(worker_id.split('.')[len(worker_id.split('.')) - 2])

def get_compatible_queues_proxy(broker, model, given):

    # Check if proxies are already made for this model and given
    if model not in broker['tasks']:
        broker['tasks'][model] = server.manager.dict()
    if str(given) not in server.broker['tasks'][model]:
        broker['tasks'][model][str(given)] = server.manager.dict()
        broker['tasks'][model][str(given)]['user_queue'] = server.manager.list()
        broker['tasks'][model][str(given)]['maintain_queue'] = server.manager.list()

    return broker['tasks'][model][str(given)]


def create_routes(server):

    @server.app.route('/{}/task'.format(server.api_version), methods=['POST'])
    def task():
        """ AUGWOP route that is hit when data needs to be added to the database
        Retrieves a json consisting of task specifications that the broker will use to assign a worker
        """
        task = request.json

        # Get model and given of task
        given = []
        for given_component in list(task['given'].keys()):
            given.append(given_component)
        model = task['models'][0]
        logger.info("Broker recieved a new user task ... adding to corresponding queue" +
            f" for given: {given} and model(s): {model}\n")

        compatible_queues_proxy = get_compatible_queues_proxy(server.broker, model, given)

        # Add to queue
        logger.info(f"Adding task for model: {model} and given: {given}...\n")
        if task['job_type'] == "UPDATE":
            compatible_queues_proxy['user_queue'].append(task)
            logger.info(f"New length of user queue: {len(compatible_queues_proxy['user_queue'])}\n")
        elif task['job_type'] == "MAINTAIN":
            compatible_queues_proxy['maintain_queue'].append(task)
            logger.info(f"New length of user queue: {len(compatible_queues_proxy['maintain_queue'])}\n")

        process_queues(server.broker)

        return Response(response=task,
                        status=200,
                        mimetype="application/json")

    @server.app.route('/{}/workers'.format(server.api_version), methods=['POST'])
    def worker():
        """ AUGWOP route responsible for interpreting HELLO messages
            and telling the broker to add this worker to the set it maintains
        """
        worker = request.json
        logger.info("Recieved HELLO message from worker {} listening on: https://localhost:{}\
                    ".format(worker['id'], worker['id'].split('.')[2]))
        if worker['id'] not in server.broker['workers']:
            server.broker['workers'][worker['id']] = server.manager.dict()
            server.broker['workers'][worker['id']]['id'] = worker['id']
            server.broker['workers'][worker['id']]['status'] = 'Idle'
            server.broker['workers'][worker['id']]['location'] = worker['location']
            server.broker['workers'][worker['id']]['given'] = server.manager.list()
            server.broker['workers'][worker['id']]['models'] = server.manager.list()
            for given in worker['qualifications'][0]['given']:
                server.broker['workers'][worker['id']]['given'].append(given)
            for model in worker['qualifications'][0]['models']:
                server.broker['workers'][worker['id']]['models'].append(model)
        else:
            logger.info("Worker: {} has been reconnected.\n".format(worker['id']))
            models = server.broker['workers'][worker['id']]['models']
            givens = server.broker['workers'][worker['id']]['given']

            # time.sleep(10)
            server.broker['workers'][worker['id']]['status'] = 'Idle'
        
        process_queues(server.broker)

        return Response(response=worker['id'],
                        status=200,
                        mimetype="application/json")

    @server.app.route('/{}/completed_task'.format(server.api_version), methods=['POST'])
    def sync_queue():
        logger.info(f"Message recieved that worker {task['worker_id']} completed task: {request.json}\n")
        process_queues(server.broker)

        return Response(response=request.json,
                        status=200,
                        mimetype="application/json")

    @server.app.route('/{}/workers/status'.format(server.api_version), methods=['GET'])
    def get_status():
        all_workers_status = []
        for worker in server.broker['workers'].items():
            status = {}
            worker_id = ".".join(worker[0].split('.')[1:])
            status[worker_id] = {}
            status[worker_id]['id'] = worker[1]['id']
            status[worker_id]['given'] = [given for given in worker[1]['given']]
            status[worker_id]['models'] = [model for model in worker[1]['models']]
            status[worker_id]['status'] = worker[1]['status']
            status[worker_id]['location'] = worker[1]['location']
            all_workers_status.append(status)

        return Response(response=json.dumps(all_workers_status),
                        status=200,
                        mimetype="application/json")

    @server.app.route('/{}/workers/remove'.format(server.api_version), methods=['POST'])
    def remove_worker():
        worker = request.json
        logger.info("Recieved a message to disconnect worker: {}\n".format(worker))
        server.broker['workers'][worker['id']]['status'] = 'Disconnected'
        return Response(response=worker,
                        status=200,
                        mimetype="application/json")

    @server.app.route('/{}/task_error'.format(server.api_version), methods=['POST'])
    def task_error():
        task = request.json
        worker_id = task['worker_id']
        # logger.error("Recieved a message that {} ran into an error on task: {}\n".format(worker_id, task))
        if worker_id in server.broker['workers']:
            if server.broker['workers'][worker_id]['status'] != 'Disconnected':
                logger.error("{} ran into error while completing task: {}\n".format(worker_id, task))
                send_task(server.broker['workers'][worker_id])
        else:
            logger.error("A previous instance of {} ran into error while completing task: {}\n".format(worker_id, task))
        return Response(response=request.json,
                        status=200,
                        mimetype="application/json")