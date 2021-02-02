#SPDX-License-Identifier: MIT
"""
Keeps data up to date
"""
import coloredlogs
from copy import deepcopy
import logging, os, time, requests
import logging.config
from multiprocessing import Process, get_start_method
from sqlalchemy.ext.automap import automap_base
import sqlalchemy as s
import pandas as pd
from sqlalchemy import MetaData

from augur.logging import AugurLogging

import warnings
warnings.filterwarnings('ignore')

logger = logging.getLogger(__name__)

class Housekeeper:

    def __init__(self, broker, augur_app):
        logger.info("Booting housekeeper")

        self._processes = []
        self.augur_logging = augur_app.logging
        self.jobs = deepcopy(augur_app.config.get_value("Housekeeper", "jobs"))
        self.orders = {
            # 0: {
            #     'switch': 0,
            #     'total_job_count': 0,
            #     'current_job_count': 0
            # }
        }
        smallest_order = 0
        for job in self.jobs:
            job['order'] = 0 if 'order' not in job or type(job['order']) != int else job['order']
            if job['order'] < smallest_order:
                smallest_order = job['order']

            if job['order'] in self.orders:
                self.orders[job['order']]['current_job_count'] += 1
                self.orders[job['order']]['total_job_count'] += 1
            else:
                self.orders[job['order']] = {
                    'switch': 0, 
                    'current_job_count': 1,
                    'total_job_count': 1
                }
        self.orders[smallest_order]['switch'] = 1
        self.broker_host = augur_app.config.get_value("Server", "host")
        self.broker_port = augur_app.config.get_value("Server", "port")
        self.broker = broker

        self.db = augur_app.database
        self.helper_db = augur_app.operations_database

        helper_metadata = MetaData()
        helper_metadata.reflect(self.helper_db, only=['worker_job'])
        HelperBase = automap_base(metadata=helper_metadata)
        HelperBase.prepare()
        self.job_table = HelperBase.classes.worker_job.__table__

        # List of tasks that need periodic updates
        self.schedule_updates()

    def schedule_updates(self):
        """ Starts update processes
        """
        self._prep_jobs()
        self.augur_logging.initialize_housekeeper_logging_listener()
        logger.info("Scheduling update processes")

        for job in self.jobs:
            process = Process(target=self.updater_process, name=job['model'], args=(
                self.broker_host, self.broker_port, self.broker, job, 
                (self.augur_logging.housekeeper_job_config, self.augur_logging.get_config())))
            self._processes.append(process)
            process.start()

    @staticmethod
    def updater_process(broker_host, broker_port, broker, job, logging_config):
        """ Controls a given plugin's update process
        """

        # Control log level
        logging.config.dictConfig(logging_config[0])
        logger = logging.getLogger(f"augur.jobs.{job['model']}")
        coloredlogs.install(level=logging_config[1]["log_level"], logger=logger, 
            fmt=logging_config[1]["format_string"])
        if logging_config[1]["quiet"]:
            logger.disabled

        def get_next_order(current_order):
            """ Get next highest job order in all current jobs, if current order is already
                the highest, then the next order would circle back to the smallest order
            """
            sorted_orders = sorted(broker['orders'].keys())
            current_index = sorted_orders.index(current_order)
            if current_index == len(broker['orders'].keys()) - 1:
                return sorted_orders[0]
            return sorted_orders[current_index + 1]

        repo_group_id = None if 'repo_group_id' not in job else job['repo_group_id']
        logger.info(f"Housekeeper spawned {job['model']} model updater process: {job}")

        try:
            compatible_worker_found = False
            # Waiting for compatible worker
            while True:

                # Must be current prioritized order to continue
                if not broker['orders'][job['order']]['switch']:
                    # print(f"no switch: {job['model']}")
                    time.sleep(3)
                    continue

                if not compatible_worker_found:
                    for worker in list(broker['workers']._getvalue().keys()):

                        if 'models' not in broker['workers'][worker] or \
                                'given' not in broker['workers'][worker]:
                            print(f"no models or no given {job['model']} {worker}")
                            print(broker['workers'][worker])
                            time.sleep(3)
                            continue
                        if job['model'] in broker['workers'][worker]['models'] and \
                                job['given'] in broker['workers'][worker]['given']:
                            compatible_worker_found = True
                    time.sleep(3)
                    continue

                logger.info("Housekeeper recognized that the broker has a worker that " + 
                    f"can handle the {job['model']} model... beginning to distribute maintained tasks")
                while True:
                    logger.info(f"Housekeeper updating {job['model']} model with given {job['given'][0]}...")
                    
                    if job['given'][0] == 'git_url' or job['given'][0] == 'github_url':
                        for repo in job['repos']:
                            if job['given'][0] == 'github_url' and 'github.com' not in repo['repo_git']:
                                continue
                            given_key = 'git_url' if job['given'][0] == 'git_url' else 'github_url'
                            task = {
                                'job_type': job['job_type'] if 'job_type' in job else "MAINTAIN", 
                                'models': [job['model']], 
                                'display_name': f"{job['model']} model for url: {repo['repo_git']}",
                                'given': {}
                            }
                            task['given'][given_key] = repo['repo_git']
                            if 'focused_task' in repo:
                                task['focused_task'] = repo['focused_task']
                            try:
                                requests.post("http://{}:{}/api/unstable/task".format(
                                    broker_host,broker_port), json=task, timeout=10)
                            except Exception as e:
                                logger.error("Error encountered: {}".format(e))

                            logger.debug(task)

                            time.sleep(15)

                    elif job['given'][0] == 'repo_group':
                        task = {
                                'job_type': job['job_type'] if 'job_type' in job else "MAINTAIN", 
                                'models': [job['model']], 
                                'display_name': f"{job['model']} model for repo group id: {repo_group_id}",
                                'given': {
                                    "repo_group": job['repos']
                                }
                            }
                        try:
                            requests.post('http://{}:{}/api/unstable/task'.format(
                                broker_host,broker_port), json=task, timeout=10)
                        except Exception as e:
                            logger.error("Error encountered: {}".format(e))

                    logger.info(f"Housekeeper finished sending {len(job['repos'])} tasks to " +
                        "the broker for it to distribute to your worker(s)")

                    broker['orders'][job['order']]['current_job_count'] -= 1

                    # while there are still maintain tasks that havent been sent to workers
                    while job['model'] not in broker['tasks'] or str(job['given']) \
                            not in broker['tasks'][job['model']]:
                        time.sleep(3)
                    while len(broker['tasks'][job['model']][str(job['given'])]['maintain_queue']) \
                            and broker['orders'][job['order']]['current_job_count']:
                        time.sleep(3)
                        continue

                    broker['orders'][job['order']]['switch'] = 0
                    next_order = get_next_order(job['order'])
                    broker['orders'][next_order]['switch'] = 1
                    broker['orders'][next_order]['current_job_count'] = broker['orders'][next_order]['total_job_count']

                    time.sleep(job['delay'])

        except KeyboardInterrupt as e:
            pass

    def join_updates(self):
        """ Join to the update processes
        """
        for process in self._processes:
            logger.debug(f"Joining {process.name} update process")
            process.join()

    def shutdown_updates(self):
        """ Ends all running update processes
        """
        for process in self._processes:
            # logger.debug(f"Terminating {process.name} update process")
            process.terminate()

    def _prep_jobs(self):
        logger.info("Preparing housekeeper jobs...\n")

        def is_invalid_job(job):
            return not ('repo_id' in job or 'repo_group_id' in job or 'repo_ids' in job)

        for job in self.jobs:

            if is_invalid_job(job):
                logger.info(f"Invalid job detected: \n{job}\n")
                continue

            if 'repo_id' in job:
                job['repo_group_id'] = None
                repoUrlSQL = s.sql.text("""
                    SELECT repo_git, repo_id FROM repo WHERE repo_id = :repo_id
                """)

                job['repos'] = pd.read_sql(repoUrlSQL, self.db, 
                    params={'repo_id': job['repo_id']}).to_dict('records')
                continue

            # If RG id is 0 then it just means to query all repos
            where_and = "AND" if job['model'] == "issues" and 'repo_group_id' in job else "WHERE"
            where_condition = "{} repo_group_id = {}".format(where_and, job['repo_group_id']
                ) if 'repo_group_id' in job and job['repo_group_id'] != 0 else '{} repo.repo_id IN ({})'.format(
                where_and, ",".join(str(id) for id in job['repo_ids'])) if 'repo_ids' in job else ''
            repo_url_sql = s.sql.text("""
                    SELECT
                        * 
                    FROM
                        (
                            ( SELECT repo_git, repo.repo_id, issues_enabled, COUNT ( * ) AS meta_count 
                            FROM repo left outer join repo_info on repo.repo_id = repo_info.repo_id
                            GROUP BY repo.repo_id, issues_enabled 
                            ORDER BY repo.repo_id ) zz
                            LEFT OUTER JOIN (
                            SELECT repo.repo_id,
                                repo.repo_name,
                                b.pull_request_count,
                                d.repo_id AS pull_request_repo_id,
                                e.last_collected,
                                (
                                b.pull_request_count - COUNT ( * )) AS pull_requests_missing,
                                ABS (
                                CAST (( COUNT ( * )) AS DOUBLE PRECISION ) / CAST ( 
                                b.pull_request_count + 1 AS DOUBLE PRECISION )) AS ratio_abs,
                                (
                                CAST (( COUNT ( * )) AS DOUBLE PRECISION ) / CAST ( 
                                b.pull_request_count + 1 AS DOUBLE PRECISION )) AS ratio_issues 
                            FROM
                                augur_data.repo left outer join  
                                augur_data.pull_requests d on d.repo_id = repo.repo_id left outer join 
                                    ( SELECT repo_id, MAX ( 
                                        data_collection_date ) AS last_collected FROM 
                                        augur_data.repo_info GROUP BY repo_id ORDER BY repo_id ) e 
                                on e.repo_id = d.repo_id left outer join 
                                augur_data.repo_info b on e.repo_id = b.repo_id and 
                                b.data_collection_date = e.last_collected
                            {}                      
                            GROUP BY
                                repo.repo_id,
                                d.repo_id,
                                b.pull_request_count,
                                e.last_collected 
                            ORDER BY ratio_abs
                            ) yy ON zz.repo_id = yy.repo_id 
                        ) D 
                    ORDER BY ratio_abs NULLS FIRST
                """.format(where_condition)) if job['model'] == "pull_requests" and 'repo_group_id' in job \
            else s.sql.text("""
                    SELECT
                        * 
                    FROM
                        (
                            ( SELECT repo_git, repo.repo_id, issues_enabled, COUNT ( * ) AS meta_count 
                            FROM repo left outer join repo_info on repo.repo_id = repo_info.repo_id
                            --WHERE issues_enabled = 'true' 
                            GROUP BY repo.repo_id, issues_enabled 
                            ORDER BY repo.repo_id ) zz
                            LEFT OUTER JOIN (
                            SELECT repo.repo_id,
                                repo.repo_name,
                                b.issues_count,
                                d.repo_id AS issue_repo_id,
                                e.last_collected,
                                COUNT ( * ) AS issues_collected_count,
                                (
                                b.issues_count - COUNT ( * )) AS issues_missing,
                                ABS (
                                CAST (( COUNT ( * )) AS DOUBLE PRECISION ) / CAST ( b.issues_count + 1 
                                AS DOUBLE PRECISION )) AS ratio_abs,
                                (
                                CAST (( COUNT ( * )) AS DOUBLE PRECISION ) / CAST ( b.issues_count + 1 
                                AS DOUBLE PRECISION )) AS ratio_issues 
                            FROM
                                augur_data.repo left outer join  
                                augur_data.pull_requests d on d.repo_id = repo.repo_id left outer join 
                                augur_data.repo_info b on d.repo_id = b.repo_id left outer join
                                ( SELECT repo_id, MAX ( data_collection_date ) AS last_collected FROM 
                                augur_data.repo_info GROUP BY repo_id ORDER BY repo_id ) e 
                                                            on e.repo_id = d.repo_id and 
                                                            b.data_collection_date = e.last_collected
                            WHERE d.pull_request_id IS NULL
                            {}
                            GROUP BY
                                repo.repo_id,
                                d.repo_id,
                                b.issues_count,
                                e.last_collected 
                            ORDER BY ratio_abs 
                            ) yy ON zz.repo_id = yy.repo_id 
                        ) D
                    ORDER BY ratio_abs NULLS FIRST
                """.format(where_condition)) if job['model'] == "issues" and 'repo_group_id' in job \
            else s.sql.text(""" 
                    SELECT repo_git, repo_id FROM repo {} ORDER BY repo_id ASC
                """.format(where_condition)) if 'order' not in job else s.sql.text(""" 
                    SELECT repo_git, repo.repo_id, count(*) as commit_count 
                    FROM augur_data.repo left outer join augur_data.commits 
                        on repo.repo_id = commits.repo_id 
                    {}
                    group by repo.repo_id ORDER BY commit_count {}
                """.format(where_condition, job['order']))
            
            reorganized_repos = pd.read_sql(repo_url_sql, self.db, params={})
            if len(reorganized_repos) == 0:
                logger.warning("Trying to send tasks for defined repo(s), but the resulting " +
                    f"query does not return any repos: {repo_url_sql}")
                job['repos'] = []
                continue

            # Update worker_job table in augur_operations
            repoIdSQL = s.sql.text("""
                    SELECT since_id_str FROM worker_job
                    WHERE job_model = :model
                """)

            job_df = pd.read_sql(repoIdSQL, self.helper_db, params={'model': job['model']})

            # If there is no job tuple found, insert one
            if len(job_df) == 0:
                job_row = {
                    'job_model': job['model'],
                    'oauth_id': 0
                }
                self.helper_db.execute(self.job_table.insert().values(job_row))
                logger.debug(f"No job tuple for {job['model']} model was found, so one was" +
                    f" inserted into the job table: {job_row}")

            # If a last id is not recorded, start from beginning of repos 
            #   (first id is not necessarily 0, but will always be >= 0)
            try:
                last_id = int(job_df.iloc[0]['since_id_str'])
            except:
                last_id = 0

            # Rearrange repos so the one after the last one that 
            #   was completed will be ran first (if prioritized ordering is not available/enabled)
            if job['model'] not in ['issues', 'pull_requests']:
                before_repos = reorganized_repos.loc[reorganized_repos['repo_id'].astype(int) < last_id]
                after_repos = reorganized_repos.loc[reorganized_repos['repo_id'].astype(int) >= last_id]

                reorganized_repos = after_repos.append(before_repos).to_dict('records')
            
            job['repos'] = reorganized_repos
