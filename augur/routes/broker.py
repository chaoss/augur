#SPDX-License-Identifier: MIT
"""
Creates routes for the broker
"""
from flask import request, jsonify, Response
import logging

def create_broker_routes(server):

    @server.app.route('/{}/job'.format(server.api_version), methods=['POST'])
    def job():
        """ AUGWOP route that is hit when data needs to be added to the database
        Retrieves a json consisting of job specifications that the broker will use to assign a worker
        """
        job = request.json
        logging.info("Recieved a new job to distribute for model: " + job['models'][0])
        # logging.info(job['given'])
        # server.broker.create_job(job)
        return jsonify({"status": "success", "job": job})

    @server.app.route('/{}/workers'.format(server.api_version), methods=['POST'])
    def worker():
        """ AUGWOP route responsible for interpreting HELLO messages
            and telling the broker to add this worker to the set it maintains
        """
        worker = request.json
        logging.info("Recieved HELLO message from worker: " + worker['id'])
        # server.broker.add_new_worker(worker, server.broker.connected_workers)
        return Response(response=worker['id'],
                        status=200,
                        mimetype="application/json")

    @server.app.route('/{}/completed_task'.format(server.api_version), methods=['POST'])
    def sync_queue():
        #job = request.json
        # logging.info("Message recieved that worker " + job['worker_id'] + " completed task: " + str(job))
        # server.broker.completed_job(job)
        return jsonify({"status": "success"})#, "job": job})

    @server.app.route('/{}/status/<worker>'.format(server.api_version), methods=['POST'])
    def get_status(worker):
        # status = server.broker.get_status(worker)
        return Response(response=status,
                        status=200,
                        mimetype="application/json")