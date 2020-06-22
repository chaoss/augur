import logging, os, sys, time, requests, json
from datetime import datetime
from multiprocessing import Process, Queue
import pandas as pd
import sqlalchemy as s
from workers.worker_base import Worker
from urllib.parse import urlparse, quote

class GitlabMergeRequestWorker(Worker):
    def __init__(self, config={}):
        # Define what this worker can be given and know how to interpret

        # given is usually either [['github_url']] or [['git_url']] (depending if your 
        #   worker is exclusive to repos that are on the GitHub platform)
        given = [['gitlab_url']]

        # The name the housekeeper/broker use to distinguish the data model this worker can fill
        #   You will also need to name the method that does the collection for this model
        #   in the format *model name*_model() such as fake_data_model() for example
        models = ['merge_requests', 'pull_request_commits', 'pull_request_files']

        # Define the tables needed to insert, update, or delete on
        #   The Worker class will set each table you define here as an attribute
        #   so you can reference all of them like self.message_table or self.repo_table
        data_tables = ['contributors', 'pull_requests',
                       'pull_request_assignees', 'pull_request_events', 'pull_request_labels',
                       'pull_request_message_ref', 'pull_request_meta', 'pull_request_repo',
                       'pull_request_reviewers', 'pull_request_teams', 'message', 'pull_request_commits',
                       'pull_request_files']
        # For most workers you will only need the worker_history and worker_job tables
        #   from the operations schema, these tables are to log worker task histories
        operations_tables = ['worker_history', 'worker_job']  # 'worker_oauth']

        # Run the general worker initialization
        self.worker_type = 'gitlab_merge_request_worker'
        super().__init__(worker_type=self.worker_type, config=config, given=given, models=models, data_tables=data_tables,
                         operations_tables=operations_tables, platform='gitlab')

        # Define data collection info
        self.tool_source = 'Gitlab Merge Request Worker'
        self.tool_version = '0.0.0'
        self.data_source = 'Gitlab API'

    def merge_requests_model(self, task, repo_id):
        self.logger.info("Querying starting ids info...\n")

        # Increment so we are ready to insert the 'next one' of each of these most recent ids
        self.history_id = self.get_max_id('worker_history', 'history_id', operations_table=True) + 1
        self.pr_id_inc = self.get_max_id('pull_requests', 'pull_request_id')
        self.pr_meta_id_inc = self.get_max_id('pull_request_meta', 'pr_repo_meta_id')

        gitlab_url = task['given']['gitlab_url']

        self.logger.info('Beginning collection of Merge Requests...\n')
        self.logger.info(f'Git URL: {gitlab_url}\n')

        owner, repo = self.get_owner_repo(gitlab_url)
        url_encoded_format_project_address = quote(owner + '/' + repo, safe='')
        url = (f'https://gitlab.com/api/v4/projects/{url_encoded_format_project_address}/merge_requests?' +
               'per_page=100&page={}')

        # Get pull requests that we already have stored
        #   Set pseudo key (something other than PK) to
        #   check dupicates with
        table = 'pull_requests'
        table_pkey = 'pull_request_id'
        update_col_map = {'pr_src_state': 'state'}
        duplicate_col_map = {'pr_src_id': 'id'}

        prs = self.paginate(url, duplicate_col_map, update_col_map, table, table_pkey,
                            where_clause='WHERE repo_id = {}'.format(repo_id),
                            value_update_col_map={}, platform='gitlab')

        # Discover and remove duplicates before we start inserting
        self.logger.info("Count of pull requests needing update or insertion: " + str(len(prs)) + "\n")
        for pr_dict in prs:

            pr = {
                'repo_id': repo_id,
                'pr_url': pr_dict['web_url'],
                'pr_src_id': pr_dict['id'],
                'pr_src_node_id': None,
                'pr_html_url': pr_dict['web_url'],
                'pr_diff_url': None,
                'pr_patch_url': None,
                'pr_issue_url': None,
                'pr_augur_issue_id': None,
                'pr_src_number': pr_dict['iid'],
                'pr_src_state': pr_dict['state'],
                'pr_src_locked': pr_dict['discussion_locked'],
                'pr_src_title': pr_dict['title'],
                'pr_augur_contributor_id': self.find_id_from_login(login=pr_dict['author']['username'], platform='gitlab'),
                'pr_body': pr_dict['description'],
                'pr_created_at': pr_dict['created_at'],
                'pr_updated_at': pr_dict['updated_at'],
                'pr_closed_at': pr_dict['closed_at'],
                'pr_merged_at': pr_dict['merged_at'],
                'pr_merge_commit_sha': pr_dict['merge_commit_sha'],
                'pr_teams': None,
                'pr_milestone': pr_dict['milestone'].get('title') if pr_dict['milestone'] else None,
                'pr_commits_url': None,
                'pr_review_comments_url': None,
                'pr_review_comment_url': None,
                'pr_comments_url': None,
                'pr_statuses_url': None,
                'pr_meta_head_id': None,
                'pr_meta_base_id': None,
                'pr_src_issue_url': None,
                'pr_src_comments_url': None,  # NOTE: this seems redundant
                'pr_src_review_comments_url': None,  # this too
                'pr_src_commits_url': None,  # this one also seems redundant
                'pr_src_statuses_url': None,
                'pr_src_author_association': None,
                'tool_source': self.tool_source,
                'tool_version': self.tool_version,
                'data_source': 'Gitlab-API'
            }

            if pr_dict['flag'] == 'need_insertion':
                self.logger.info(f'PR {pr_dict["id"]} needs to be inserted\n')

                result = self.db.execute(self.pull_requests_table.insert().values(pr))
                self.logger.info(f"Added Pull Request: {result.inserted_primary_key}")
                self.pr_id_inc = int(result.inserted_primary_key[0])

            elif pr_dict['flag'] == 'need_update':
                result = self.db.execute(self.pull_requests_table.update().where(
                    self.pull_requests_table.c.pr_src_id == pr_dict['id']).values(pr))
                self.logger.info("Updated tuple in the pull_requests table with existing pr_src_id: {}".format(
                    pr_dict['id']))
                self.pr_id_inc = pr_dict['pkey']

            else:
                self.logger.info("PR does not need to be inserted. Fetching its id from DB")
                pr_id_sql = s.sql.text("""
                            SELECT pull_request_id FROM pull_requests
                            WHERE pr_src_id={}
                        """.format(pr_dict['id']))

                self.pr_id_inc = int(pd.read_sql(pr_id_sql, self.db).iloc[0]['pull_request_id'])

            self.query_labels(pr_dict['labels'], self.pr_id_inc, url_encoded_format_project_address)

            '''
            self.query_pr_events(owner, repo, pr_dict['number'], self.pr_id_inc)
            self.query_pr_comments(owner, repo, pr_dict['number'], self.pr_id_inc)
            self.query_reviewers(pr_dict['requested_reviewers'], self.pr_id_inc)
            self.query_pr_meta(pr_dict['head'], pr_dict['base'], self.pr_id_inc)
            '''
            self.logger.info(f"Inserted PR data for {owner}/{repo}")
            self.results_counter += 1

        self.register_task_completion(task, repo_id, 'pull_requests')

    def query_labels(self, labels, pr_id, project_address_encoded):
        self.logger.info('Querying PR Labels\n')

        if len(labels) == 0:
            self.logger.info('No new labels to add\n')
            return

        label_list = []
        for label in labels:
            url = f'https://gitlab.com/api/v4/projects/{project_address_encoded}/labels/{label}'
            r = requests.get(url=url, headers=self.headers)
            self.update_gitlab_rate_limit(r)
            label_list.append(r.json())
        labels = label_list
        table = 'pull_request_labels'
        duplicate_col_map = {'pr_src_id': 'id'}
        update_col_map = {}
        table_pkey = 'pr_label_id'

        update_keys = list(update_col_map.keys()) if update_col_map else []
        cols_query = list(duplicate_col_map.keys()) + update_keys + [table_pkey]

        pr_labels_table_values = self.get_table_values(cols_query, [table])

        new_labels = self.assign_tuple_action(labels, pr_labels_table_values, update_col_map, duplicate_col_map,
                                              table_pkey)

        self.logger.info(f'Found {len(new_labels)} labels\n')
        for label_dict in new_labels:

            label = {
                'pull_request_id': pr_id,
                'pr_src_id': label_dict['id'],
                'pr_src_node_id': None,
                'pr_src_url': None,
                'pr_src_description': label_dict['description'],
                'pr_src_color': label_dict['color'],
                'pr_src_default_bool': label_dict['is_project_label'],
                'tool_source': self.tool_source,
                'tool_version': self.tool_version,
                'data_source': self.data_source
            }

            if label_dict['flag'] == 'need_insertion':
                result = self.db.execute(self.pull_request_labels_table.insert().values(label))
                self.logger.info(f"Added PR Label: {result.inserted_primary_key}\n")
                self.logger.info(f"Inserted PR Labels data for PR with id {pr_id}\n")

                self.results_counter += 1

    def fake_data_model(self, task, repo_id):
        """ This is just an example of a data collection method. All data collection 
            methods for all workers currently accept this format of parameters. If you 
            want to change these parameters, you can re-define the collect() method to 
            overwrite the Worker class' version of it (which is the method that calls
            this method).

            :param task: the task generated by the housekeeper and sent to the broker which 
            was then sent to this worker. Takes the example dict format of:
                {
                    'job_type': 'MAINTAIN', 
                    'models': ['fake_data'], 
                    'display_name': 'fake_data model for url: https://github.com/vmware/vivace',
                    'given': {
                        'git_url': 'https://github.com/vmware/vivace'
                    }
                }
            :param repo_id: the collect() method queries the repo_id given the git/github url
            and passes it along to make things easier. An int such as: 27869
        """

        # Collection and insertion of data happens here

        # ...

        # Register this task as completed.
        #   This is a method of the worker class that is required to be called upon completion
        #   of any data collection model, this lets the broker know that this worker is ready
        #   for another task
        self.register_task_completion(task, repo_id, 'fake_data')
