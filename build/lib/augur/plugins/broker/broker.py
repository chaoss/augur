import requests
from multiprocessing import Process, Queue

import json
import random
import sys
import time

import click
import zmq
import multiprocessing

import logging
logging.basicConfig(filename='broker.log', level=logging.INFO)

# from multichannel.worker_tasks import deep_github_worker_task, github_worker_task, facade_worker_task
# from multichannel.client_tasks import client_owner_repo_task, client_git_url_task
NBR_WORKERS = 1
NBR_CLIENTS = 1

class Worker():
    """Workers collect data from data sources, normalize the data into our schema, and update the database. 
    When workers connect, they advertise what kind of work they can accept using a specification as detailed above. 
    Workers with the same ID (i.e. of the same type) share a job queue. 
    When workers with different IDs can accept the same job, each of those workers will be assigned a copy of the job.
    Workers are language agnostic: so long as they can connect to the broker and to the database, they’re good to go.
    
    ID: what the broker will be able to reference a worker as
    location: the url of the server a worker is working on
    qualifications: consists of the given and model a worker is able to provide data about
    """
    def __init__(self, id, location=None, qualifications=None):
        self.id = id
        self.location = location
        self.qualifications = qualifications
        if qualifications is not None:
            self.given = qualifications[0]['given'][0][0]
            self.models = qualifications[0]['models']
        print("Worker given: " + self.id)
        self.queue = Queue()

class Job():
    """ Defines the instructions to give to a worker about the data needed to be inserted in our database
    
    job_type: type of action worker should take in reference to models and given
    models: references a sector of data that the worker is able to provide
    given: what the worker is given and is able to provide data about
    """
    def __init__(self, job_type, models, given):
        self.job_type = job_type
        self.models = models
        self.given = given

class Broker(object):
    """The broker is responsible for queuing and distributing requests to workers. 
    These requests come from the server and are for data that is to be used in the calculation of a metric. 

    A worker provides data from a singular data source: each worker that 
        provides data from the same data source is of the same “type.” 
    
    Each type of worker gets their own queue, and workers compete against other workers of 
        their own type (competing consumers) to fulfill jobs on that queue. 
    """

    def __init__(self):
        """ Initialize the broker's maintained sets of connected workers and created jobs
        """
        # self.NBR_CLIENTS = 1
        self.num_workers = 1
        self.connected_workers = {'com.augurlabs.core.github_worker': Worker(id='com.augurlabs.core.github_worker')}
        self.created_jobs = []
        logging.info("Broker spawned and is ready to accept tasks.")

    def add_new_worker(self, worker):
        """ Method to add a new worker to the set of workers the broker is managing
        """
        self.connected_workers[worker['id']] = (Worker(id=worker['id'], location=worker['location'], qualifications=worker['qualifications']))
        logging.info("Recieved worker and opened up pool to hold sockets")
        pool = multiprocessing.Pool()

        pool.apply_async(self.main(), ())

    def create_job(self, job_received):
        """ Method to add a job to the brokers set of maintained jobs and find compatible workers for it
        Hits compatible workers' AUGWOP endpoints that adds the job to their queues
        """
        # self.created_jobs.append(Job(job_type=job['job_type'], models=job['models'], given=job["given"]))

        # job = Job(job_type=job_received['job_type'], models=job_received['models'], given=job_received["given"])
        # for job in self.created_jobs:
        given = list(job_received['given'].keys())[0]
        model = job_received['models'][0]
        # print(self.connected_workers)
        # print(model in self.connected_workers['com.augurlabs.core.github_worker'].models, model, worker.models)
        compatible_workers = [worker for worker in self.connected_workers.values() if worker.given == given and model in worker.models]

        for worker in compatible_workers:

            """ PRIORITY KEY:
                0 - user/endpoint created job ("UPDATE" job type)
                1 - a maintained job created by the housekeeper ("MAINTAIN" job type)
            """

            if job_received['job_type'] == "UPDATE":
                self.connected_workers[worker.id].queue.put(job_received)
            elif job_received['job_type'] == "MAINTAIN":
                self.connected_workers[worker.id].queue.put(job_received)

            print(worker.id + "'s queue after adding the job: ")
            print(dump_queue(self.connected_workers[worker.id].queue))

            requests.post(worker.location + '/AUGWOP/task', json=job_received)

    def completed_job(self, job):
        completed_job = self.connected_workers[job['worker_id']].queue.get()
        logging.info("Job completed: ", job)

    def main(self):
        """Load balancer main loop."""
        # Prepare context and sockets
        
        context = zmq.Context.instance()
        frontend = context.socket(zmq.ROUTER)
        frontend.bind("ipc://frontend.ipc")
        backend = context.socket(zmq.ROUTER)
        # backend.bind("ipc://backend.ipc")
        backend.bind("tcp://*:5558")

        # Start background tasks
        def start(task, *args):
            process = multiprocessing.Process(target=task, args=args)
            process.daemon = True
            process.start()

        # for i in range(NBR_WORKERS):
        #     start(github_worker_task, i)
        #     start(facade_worker_task, i)
        # for i in range(NBR_CLIENTS):
        #     start(client_git_url_task, i)
        #     start(client_owner_repo_task, i)

        # Initialize main loop state
        count = NBR_CLIENTS
        workers = []
        jobs = {}
        client_job_ids = {}
        poller = zmq.Poller()
        # Only poll for requests from backend 
        poller.register(backend, zmq.POLLIN)
        logging.info("Beginning to listen...")
        while True:
            # Identify which sockets have activity
            # sockets = dict(poller.poll(1000))
            # logging.info("about to start" + str(sockets))

            # if sockets:
            #     # If the backend is the one that has activity
            #     if backend in sockets:
            # Identify the worker and the client
            backend.recv()
            request = backend.recv_multipart()
            logging.info("REQUEST: " + str(request) + str(type(request[len(request) - 1])))
            # worker, delimiter, client = request[:3]

            # parse the message
            message = request[len(request) - 1].decode('ascii').split(" ")
            sender = request[0].decode('ascii')#.split(" ")
            logging.info("Parsed message: " + str(message) + str(type(message)))

            # If there are no workers currently available
            # if not workers:
                #listen on the frontend now that a worker is available (we just found one above)
                # poller.register(frontend, zmq.POLLIN)

            if 'HELLO' == message[0]:
                spec = json.loads(message[1])

                # Create a new augur worker
                augur_worker = AugurWorker(ID=worker,
                                           given=spec['qualifications'][0]['given'][0],
                                           models=spec['qualifications'][0]['models'])

                # Add new worker to the list of available workers
                workers.append(augur_worker)

            # If the client's message is not READY and there are more than 3 parts to it, then that mean's a reply to a request
            if client != b"READY" and len(request) > 3:
                # Identify the reply
                delimiter, reply = request[3:]

                if 'DONE' == reply.decode('ascii'):
                    job_items = list(jobs.items())
                    job_id = next(job[0] for job in job_items if worker.decode('ascii') in list(job[1].keys()))

                    jobs[job_id][worker.decode('ascii')] = 'complete'

                    if len([job for job in jobs[job_id].values()]) == len([job for job in jobs[job_id].values() if job == 'complete']):
                        logging.info(f"Job {job_id} is finished")
                        frontend.send_multipart([client_job_ids[job_id], b"", b"DONE"])
                    else:
                        logging.info(f"Job {job_id} is still in progress")

                # Send to the client that made the request the contents of the reply 
                frontend.send_multipart([client, b"", reply])

                # Note that one of the requests has been served
                count -= 1

                # # If there are no more requests to be served, terminate
                # if not count:
                #     break

        # If there's activity on the frontend
        if frontend in sockets:
            # Get next client request
            msg = frontend.recv_multipart()
            client = msg[0]
            delimiter = msg[1]
            request = msg[2]

            # Identify given from request
            given = list(json.loads((request.decode('ascii')).split(" ")[1])['given'])[0]

            # Find workers that can process that given
            compatible_workers = [worker for worker in workers if worker.given[1] == given]

            # If any exist, give each one a copy of the request
            if workers is not None:
                job_id = random.randint(0, 100)
                jobs[job_id] = {}
                client_job_ids[job_id] = client
                logging.info(f"Created job {job_id} for {client.decode('ascii')}")
                for worker in compatible_workers:
                    # Send to the backend the worker to use, which client requested, and the message from the client
                    #logging.info(f"{request.decode('ascii')} is being routed to {worker.ID.decode('ascii')}")
                    backend.send_multipart([worker.ID, b"", client, b"", request])

                    # Add the job to the list of current jobs
                    jobs[job_id][worker.ID.decode('ascii')] = 'working'

            # Otherwise, let the frontend know that the request can't be served
            else:
                logging.warning(f"Augur does not have knowledge of any workers that are capable of handing the request {request.decode('ascii')}. \nPlease install a worker that can serve requests given `{given}`")
                frontend.send_multipart([client, b"", b"NO-WORKERS"])
            # else:
            #     logging.info("TIMEOUT")

        # Clean up
        backend.close()
        frontend.close()
        context.term()

def dump_queue(queue):
    """
    Empties all pending items in a queue and returns them in a list.
    """
    result = []
    queue.put("STOP")

    for i in iter(queue.get, 'STOP'):
        result.append(i)
    # time.sleep(.1)
    return result

