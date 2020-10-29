#SPDX-License-Identifier: MIT
""" Helper methods constant across all workers """
import requests, datetime, time, traceback, json, os, sys, math, logging, numpy, copy
from logging import FileHandler, Formatter, StreamHandler
from multiprocessing import Process, Queue
import sqlalchemy as s
import pandas as pd
from pathlib import Path
from urllib.parse import urlparse, quote
from augur.config import AugurConfig
from augur.logging import AugurLogging
from sqlalchemy.sql.expression import bindparam
from augur.platform_connector import PlatformConnector

class Worker(PlatformConnector):

    def __init__(self, worker_type, config={}, given=[], models=[], data_tables=[], operations_tables=[], platform="github"):

        # PlatformConnector.__init__(config, given, data_tables, operations_tables, platform)
        super(Worker, self).__init__(config, given, data_tables, operations_tables, platform)

        self.worker_type = worker_type
        self.collection_start_time = None

        self._task = None # task currently being worked on (dict)
        self.worker_type = worker_type
        self._child = None # process of currently running task (multiprocessing process)
        self._queue = Queue() # tasks stored here 1 at a time (in a mp queue so it can translate across multiple processes)

        # count of tuples inserted in the database (to store stats for each task in op tables)
        self.update_counter = 0
        self.insert_counter = 0
        self._results_counter = 0

        # if we are finishing a previous task, certain operations work differently
        self.finishing_task = False

        self.config = {
                'worker_type': self.worker_type,
                'host': self.augur_config.get_value("Server", "host"),
                'offline_mode': False
            }

        try:
            worker_defaults = self.augur_config.get_default_config()['Workers'][self.config['worker_type']]
            self.config.update(worker_defaults)
        except KeyError as e:
            logging.warn('Could not get default configuration for {}'.format(self.config['worker_type']))

        worker_info = self.augur_config.get_value('Workers', self.config['worker_type'])
        self.config.update(worker_info)

        worker_port = self.config['port']
        while True:
            try:
                r = requests.get('http://{}:{}/AUGWOP/heartbeat'.format(
                    self.config['host'], worker_port)).json()
                if 'status' in r:
                    if r['status'] == 'alive':
                        worker_port += 1
            except:
                break

        self.config.update({ 
            'port': worker_port,
            'id': "workers.{}.{}".format(self.worker_type, worker_port),
            "capture_output": False,
            'location': 'http://{}:{}'.format(self.config['host'], worker_port),
            'port_broker': self.augur_config.get_value('Server', 'port'),
            'host_broker': self.augur_config.get_value('Server', 'host'),
        })
        self.config.update(config)

        # Initialize logging in the main process
        self.initialize_logging()

        # Clear log contents from previous runs
        open(self.config["server_logfile"], "w").close()
        open(self.config["collection_logfile"], "w").close()

        # Get configured collection logger
        self.logger = logging.getLogger(self.config["id"])
        self.logger.info('Worker (PID: {}) initializing...'.format(str(os.getpid())))

        self.models = models
        self.specs = {
            'id': self.config['id'], # what the broker knows this worker as
            'location': self.config['location'], # host + port worker is running on (so broker can send tasks here)
            'qualifications':  [
                {
                    'given': self.given, # type of repo this worker can be given as a task
                    'models': self.models # models this worker can fill for a repo as a task
                }
            ],
            'config': self.config
        }

        # Send broker hello message
        if self.config['offline_mode'] is False:
            self.connect_to_broker()

        try:
            self.tool_source
            self.tool_version
            self.data_source
        except:
            self.tool_source = 'Augur Worker Testing'
            self.tool_version = '0.0.0'
            self.data_source = 'Augur Worker Testing'

    def __repr__(self):
        return f"{self.config['id']}"

    def initialize_logging(self):
<<<<<<< HEAD
        self.config['log_level'] = self.config['log_level'].upper()
        if self.config['debug']:
            self.config['log_level'] = 'DEBUG'

        if self.config['verbose']:
=======

        super(Worker, self).initialize_logging()

        if "verbose" in self.config and self.config["verbose"]:
>>>>>>> d01c121e... Automatically add repos to org
            format_string = AugurLogging.verbose_format_string
        else:
            format_string = AugurLogging.simple_format_string
    
        formatter = Formatter(fmt=format_string)
        error_formatter = Formatter(fmt=AugurLogging.error_format_string)

        worker_dir = AugurLogging.get_log_directories(self.augur_config, reset_logfiles=False) + "/workers/"
        Path(worker_dir).mkdir(exist_ok=True)
        logfile_dir = worker_dir + f"/{self.worker_type}/"
        Path(logfile_dir).mkdir(exist_ok=True)

        server_logfile = logfile_dir + '{}_{}_server.log'.format(self.worker_type, self.config["port"])
        collection_logfile = logfile_dir + '{}_{}_collection.log'.format(self.worker_type, self.config["port"])
        collection_errorfile = logfile_dir + '{}_{}_collection.err'.format(self.worker_type, self.config["port"])
        self.config.update({
            'logfile_dir': logfile_dir,
            'server_logfile': server_logfile,
            'collection_logfile': collection_logfile,
            'collection_errorfile': collection_errorfile
        })

        collection_file_handler = FileHandler(filename=self.config['collection_logfile'], mode="a")
        collection_file_handler.setFormatter(formatter)
        collection_file_handler.setLevel(self.config['log_level'])

        collection_errorfile_handler = FileHandler(filename=self.config['collection_errorfile'], mode="a")
        collection_errorfile_handler.setFormatter(error_formatter)
        collection_errorfile_handler.setLevel(logging.WARNING)

        logger = logging.getLogger(self.config['id'])
        logger.handlers = []
        logger.addHandler(collection_file_handler)
        logger.addHandler(collection_errorfile_handler)
        logger.setLevel(self.config['log_level'])
        logger.propagate = False

<<<<<<< HEAD
        if self.config['debug']:
            self.config['log_level'] = 'DEBUG'
=======
        if "debug" in self.config and self.config["debug"]:
            self.config["log_level"] = "DEBUG"
>>>>>>> d01c121e... Automatically add repos to org
            console_handler = StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(self.config['log_level'])
            logger.addHandler(console_handler)

<<<<<<< HEAD
        if self.config['quiet']:
=======
        if "quiet" in self.config and self.config["quiet"]:
>>>>>>> d01c121e... Automatically add repos to org
            logger.disabled = True

        self.logger = logger

    @property
    def results_counter(self):
        """ Property that is returned when the worker's current results_counter is referenced
        """
        if self.worker_type == 'facade_worker':
            return self.cfg.repos_processed #TODO: figure out why this doesn't work...
        else:
            return self._results_counter

    @results_counter.setter
    def results_counter(self, value):
        """ entry point for the broker to add a task to the queue
        Adds this task to the queue, and calls method to process queue
        """
        self._results_counter = value

    @property
    def task(self):
        """ Property that is returned when the worker's current task is referenced
        """
        return self._task

    @task.setter
    def task(self, value):
        """ entry point for the broker to add a task to the queue
        Adds this task to the queue, and calls method to process queue
        """
        # If the task has one of our "valid" job types
        if value['job_type'] == "UPDATE" or value['job_type'] == "MAINTAIN":
            self._queue.put(value)

        # Setting that causes paginating through ALL pages, not just unknown ones
        # This setting is set by the housekeeper and is attached to the task before it gets sent here
        if 'focused_task' in value:
            if value['focused_task'] == 1:
                self.logger.debug("Focused task is ON\n")
                self.finishing_task = True

        self._task = value
        self.run()

    def cancel(self):
        """ Delete/cancel current task
        """
        self._task = None

    def run(self):
        """ Kicks off the processing of the queue if it is not already being processed
        Gets run whenever a new task is added
        """
        # Spawn a subprocess to handle message reading and performing the tasks
        self._child = Process(target=self.collect, args=())
        self._child.start()

    def collect(self):
        """ Function to process each entry in the worker's task queue
        Determines what action to take based off the message type
        """
        self.initialize_logging() # need to initialize logging again in child process cause multiprocessing
        self.logger.info("Starting data collection process\n")
        self.initialize_database_connections()
        while True:
            if not self._queue.empty():
                message = self._queue.get() # Get the task off our MP queue
            else:
                self.logger.info("No job found.")
                break
            self.logger.info("Popped off message: {}\n".format(str(message)))

            if message['job_type'] == 'STOP':
                break

            # If task is not a valid job type
            if message['job_type'] != 'MAINTAIN' and message['job_type'] != 'UPDATE':
                raise ValueError('{} is not a recognized task type'.format(message['job_type']))
                pass

            # Query repo_id corresponding to repo url of given task
            repoUrlSQL = s.sql.text("""
                SELECT min(repo_id) as repo_id FROM repo WHERE repo_git = '{}'
                """.format(message['given'][self.given[0][0]]))
            repo_id = int(pd.read_sql(repoUrlSQL, self.db, params={}).iloc[0]['repo_id'])
            self.logger.info("repo_id for which data collection is being initiated: {}".format(str(repo_id)))
            # Call method corresponding to model sent in task
            try:
                model_method = getattr(self, '{}_model'.format(message['models'][0]))
                self.record_model_process(repo_id, 'repo_info')
            except Exception as e:
                self.logger.error('Error: {}.\nNo defined method for model: {}, '.format(e, message['models'][0]) +
                    'must have name of {}_model'.format(message['models'][0]))
                self.register_task_failure(message, repo_id, e)
                break

            # Model method calls wrapped in try/except so that any unexpected error that occurs can be caught
            #   and worker can move onto the next task without stopping
            try:
                self.logger.info("Calling model method {}_model".format(message['models'][0]))
                model_method(message, repo_id)
            except Exception as e: # this could be a custom exception, might make things easier
                self.register_task_failure(message, repo_id, e)
                break

        self.logger.debug('Closing database connections\n')
        self.db.dispose()
        self.helper_db.dispose()
        self.logger.info("Collection process finished")

    def sync_df_types(self, subject, source, subject_columns, source_columns):

        type_dict = {}
        for index in range(len(source_columns)):
            if type(source[source_columns[index]].values[0]) == numpy.datetime64:
                subject[subject_columns[index]] = pd.to_datetime(subject[subject_columns[index]], utc=True)
                source[source_columns[index]] = pd.to_datetime(
                    source[source_columns[index]], utc=True)
                continue
            type_dict[subject_columns[index]] = type(source[source_columns[index]].values[0])

        subject.astype(type_dict)
        
        return subject, source

    def organize_needed_data(self, new_data, table_values, table_pkey, action_map={}):

        if len(table_values) == 0:
            return new_data, []

        if len(new_data) == 0:
            return [], []

        need_insertion = pd.DataFrame()
        need_updates = pd.DataFrame()

        table_values_df = pd.DataFrame(table_values, columns=table_values[0].keys())
        new_data_df = pd.DataFrame(new_data).dropna(subset=action_map['insert']['source'])

        new_data_df, table_values_df = self.sync_df_types(new_data_df, table_values_df, 
                action_map['insert']['source'], action_map['insert']['augur'])

        need_insertion = new_data_df.merge(table_values_df, suffixes=('','_table'),
                how='outer', indicator=True, left_on=action_map['insert']['source'],
                right_on=action_map['insert']['augur']).loc[lambda x : x['_merge']=='left_only']

        if 'update' in action_map:
            new_data_df, table_values_df = self.sync_df_types(new_data_df, table_values_df, 
                action_map['update']['source'], action_map['update']['augur'])
            
            need_updates = new_data_df.merge(table_values_df, left_on=action_map['insert']['source'],
                right_on=action_map['insert']['augur'], suffixes=('','_table'), 
                how='inner',indicator=False).merge(table_values_df, left_on=action_map['update']['source'],
                right_on=action_map['update']['augur'], suffixes=('','_table'), how='outer', indicator=True
                                ).loc[lambda x : x['_merge']=='left_only']

            need_updates = need_updates.drop([column for column in list(need_updates.columns) if \
                column not in action_map['update']['augur'] and column not in action_map['insert']['augur']], 
                axis='columns')

            for column in action_map['insert']['augur']:
                need_updates[f'b_{column}'] = need_updates[column]

            need_updates = need_updates.drop([column for column in action_map['insert']['augur']], axis='columns')

        self.logger.info(f'Page needs {len(need_insertion)} insertions and '
            f'{len(need_updates)} updates.\n')

        return need_insertion.to_dict('records'), need_updates.to_dict('records')

    def assign_tuple_action(self, new_data, table_values, update_col_map, duplicate_col_map, table_pkey, value_update_col_map={}):
        """ Include an extra key-value pair on each element of new_data that represents
            the action that should be taken with this element (i.e. 'need_insertion')

        :param new_data: List of dictionaries, data to be assigned an action to
        :param table_values: Pandas DataFrame, existing data in the database to check
            what action should be taken on the new_data depending on the presence of
            each element in this DataFrame
        :param update_col_map: Dictionary, maps the column names of the source data
            to the field names in our database for columns that should be checked for
            updates (if source data value != value in existing database row, then an
            update is needed). Key is source data column name, value is database field name.
            Example: {'id': 'gh_issue_id'}
        :param duplicate_col_map: Dictionary, maps the column names of the source data
            to the field names in our database for columns that should be checked for
            duplicates (if source data value == value in existing database row, then this
            element is a duplicate and would not need an insertion). Key is source data
            column name, value is database field name. Example: {'id': 'gh_issue_id'}
        :param table_pkey: String, the field name of the primary key of the table in
            the database that we are checking the table_values for.
        :param value_update_col_map: Dictionary, sometimes we add a new field to a table,
            and we want to trigger an update of that row in the database even if all of the
            data values are the same and would not need an update ordinarily. Checking for
            a specific existing value in the database field allows us to do this. The key is the
            name of the field in the database we are checking for a specific value to trigger
            an update, the value is the value we are checking for equality to trigger an update.
            Example: {'cntrb_id': None}
        :return: List of dictionaries, contains all the same elements of new_data, except
            each element now has an extra key-value pair with the key being 'flag', and
            the value being 'need_insertion', 'need_update', or 'none'
        """
        need_insertion_count = 0
        need_update_count = 0

        if type(table_values) == list:
            if len(table_values) > 0:
                table_values = pd.DataFrame(table_values, columns=table_values[0].keys())
            else:
                table_values = pd.DataFrame(table_values)

        for i, obj in enumerate(new_data):
            if type(obj) != dict:
                new_data[i] = {'flag': 'none'}
                continue

            obj['flag'] = 'none' # default of no action needed
            existing_tuple = None
            for db_dupe_key in list(duplicate_col_map.keys()):

                if table_values.isin([obj[duplicate_col_map[db_dupe_key]]]).any().any():
                    if table_values[table_values[db_dupe_key].isin(
                        [obj[duplicate_col_map[db_dupe_key]]])].to_dict('records'):

                        existing_tuple = table_values[table_values[db_dupe_key].isin(
                            [obj[duplicate_col_map[db_dupe_key]]])].to_dict('records')[0]
                    continue

                obj['flag'] = 'need_insertion'
                need_insertion_count += 1
                break

            if obj['flag'] == 'need_insertion':
                continue

            if not existing_tuple:
                self.logger.info('An existing tuple was not found for this data ' +
                    'point and we have reached the check-updates portion of assigning ' +
                    'tuple action, so we will now move to next data point\n')
                continue

            # If we need to check the values of the existing tuple to determine if an update is needed
            for augur_col, value_check in value_update_col_map.items():
                not_nan_check = not (math.isnan(value_check) and math.isnan(existing_tuple[augur_col])) if value_check is not None else True
                if existing_tuple[augur_col] != value_check and not_nan_check:
                    continue
                self.logger.info("Found a tuple that needs an update for column: {}\n".format(augur_col))
                obj['flag'] = 'need_update'
                obj['pkey'] = existing_tuple[table_pkey]
                need_update_count += 1

            if obj['flag'] == 'need_update':
                self.logger.info('Already determined that current tuple needs update, skipping checking further updates. '
                    'Moving to next tuple.\n')
                continue

            # Now check the existing tuple's values against the response values to determine if an update is needed
            for col in update_col_map.keys():
                if update_col_map[col] not in obj:
                    continue
                if obj[update_col_map[col]] == existing_tuple[col]:
                    continue
                self.logger.info("Found a tuple that needs an update for column: {}\n".format(col))
                obj['flag'] = 'need_update'
                self.logger.info(existing_tuple)
                obj['pkey'] = existing_tuple[table_pkey]
                need_update_count += 1

        self.logger.info("Page recieved has {} tuples, while filtering duplicates this ".format(len(new_data)) +
            "was reduced to {} tuples, and {} tuple updates are needed.\n".format(need_insertion_count, need_update_count))
        return new_data

    def connect_to_broker(self):
        connected = False
        for i in range(5):
            try:
                self.logger.debug("Connecting to broker, attempt {}\n".format(i))
                if i > 0:
                    time.sleep(10)
                self.logger.info("broker & port: "+self.config['host_broker']+"  "+self.config['port_broker'])
                requests.post('http://{}:{}/api/unstable/workers'.format(
                    self.config['host_broker'],self.config['port_broker']), json=self.specs)
                self.logger.info("Connection to the broker was successful\n")
                connected = True
                break
            except requests.exceptions.ConnectionError:
                self.logger.error('Cannot connect to the broker. Trying again...\n')
        if not connected:
            sys.exit('Could not connect to the broker after 5 attempts! Quitting...\n')

    @staticmethod
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

    def bulk_insert(self, table, insert=[], update=[], unique_columns=[], update_columns=[]):
        
        self.logger.info(f"{len(insert)} insertions are needed and {len(update)} "
            f"updates are needed for {table}\n")

        update_result = None
        insert_result = None

        if len(update) > 0:
            success = False
            update_start_time = time.time()
            while not success:
                try:
                    update_result = self.db.execute(
                        table.update().where(
                                eval(' and '.join([f"self.{table}_table.c.{key} == bindparam('b_{key}')" for \
                                    key in unique_columns]))
                            ).values(
                                {key: key for key in update_columns}
                            ),
                        update
                    )
                    success = True
                except Exception as e:
                    self.logger.info('error: {}'.format(e))
                    time.sleep(5)

            self.update_counter += update_result.rowcount
            self.logger.info(f"Updated {update_result.rowcount} rows in "
                f"{time.time() - update_start_time} seconds")

        if len(insert) > 0:
            success = False
            insert_start_time = time.time()
            while not success:
                try:
                    insert_result = self.db.execute(
                        table.insert(),
                        insert
                    )
                    success = True
                except Exception as e:
                    self.logger.info('error: {}'.format(e))
                    time.sleep(5)

            self.insert_counter += insert_result.rowcount
            self.logger.info(f"Inserted {insert_result.rowcount} rows in "
                f"{time.time() - insert_start_time} seconds")

        return insert_result, update_result

    def enrich_data_primary_keys(self, source_data, table, gh_merge_fields, augur_merge_fields):

        self.logger.info("Preparing to enrich data.\n")

        if len(source_data) == 0:
            self.logger.info("There is no source data to enrich.\n")
            return []

        source_df = pd.DataFrame(source_data)
        # temp_dict = {field: str(table) for field in augur_merge_fields}

        s_tuple = s.tuple_([table.c[field] for field in augur_merge_fields])
        s_tuple.__dict__['clauses'] = s_tuple.__dict__['clauses'][0].effective_value
        s_tuple.__dict__['_type_tuple'] = []
        for field in augur_merge_fields:
            s_tuple.__dict__['_type_tuple'].append(table.c[field].__dict__['type'])

        for column in gh_merge_fields:
            if '.' not in column:
                continue
            root = column.split('.')[0]
            expanded_column = pd.DataFrame(source_df[root].tolist())
            expanded_column.columns = [f'{root}.{attribute}' for attribute in expanded_column.columns]
            source_df = source_df.join(expanded_column)

        primary_keys = self.db.execute(s.sql.select(
                [table.c[field] for field in augur_merge_fields] + [table.c[list(table.primary_key)[0].name]]
            ).where(
                s_tuple.in_(
                # eval("""s.tuple_(', '.join([f"self.{table}_table.c['{field}']" for field, table in temp_dict.items()]))""").in_(
                    list(source_df[gh_merge_fields].itertuples(index=False))
                ))).fetchall()

        if len(primary_keys) > 0:
            primary_keys_df = pd.DataFrame(primary_keys, 
                columns=augur_merge_fields + [list(table.primary_key)[0].name])
        else:
            self.logger.info("There are no inserted primary keys to enrich the source data with.\n")
            return source_data

        source_df, primary_keys_df = self.sync_df_types(source_df, primary_keys_df, 
                gh_merge_fields, augur_merge_fields)

        return json.loads(source_df.merge(primary_keys_df, suffixes=('','_table'),
            how='inner', left_on=gh_merge_fields, right_on=augur_merge_fields).to_json(
            default_handler=str, orient='records'))

    def paginate_endpoint(self, url, action_map={}, table=None, where_clause=True, platform='github'):

        table_values = self.db.execute(s.sql.select(self.get_relevant_columns(
            table, action_map)).where(where_clause)).fetchall()

        page_number = 1
        multiple_pages = False
        need_insertion = []
        need_update = []
        all_data = []
        forward_pagination = True
        backwards_activation = False
        last_page_number = -1
        while True:

            # Multiple attempts to hit endpoint
            num_attempts = 0
            success = False
            while num_attempts < 3:
                self.logger.info(f"Hitting endpoint: {url.format(page_number)}...\n")
                response = requests.get(url=url.format(page_number), headers=self.headers)

                self.update_rate_limit(response, platform=platform)

                try:
                    page_data = response.json()
                except:
                    page_data = json.loads(json.dumps(response.text))

                if type(page_data) == list:
                    success = True
                    break
                elif type(page_data) == dict:
                    self.logger.info("Request returned a dict: {}\n".format(page_data))
                    if page_data['message'] == "Not Found":
                        self.logger.warning(
                            f"Github repo was not found or does not exist for endpoint: {url.format(page_number)}\n")
                        break
                    if "You have triggered an abuse detection mechanism." in page_data['message']:
                        num_attempts -= 1
                        self.update_rate_limit(response, temporarily_disable=True,platform=platform)
                    if page_data['message'] == "Bad credentials":
                        self.update_rate_limit(response, bad_credentials=True, platform=platform)
                elif type(page_data) == str:
                    self.logger.info(f"Warning! page_data was string: {page_data}\n")
                    if "<!DOCTYPE html>" in page_data:
                        self.logger.info("HTML was returned, trying again...\n")
                    elif len(page_data) == 0:
                        self.logger.warning("Empty string, trying again...\n")
                    else:
                        try:
                            page_data = json.loads(page_data)
                            success = True
                            break
                        except:
                            pass
                num_attempts += 1
            if not success:
                break

            # Success

            # Determine if continued pagination is needed

            if len(page_data) == 0:
                self.logger.info("Response was empty, breaking from pagination.\n")
                break

            all_data += page_data

            if not forward_pagination:

                # Checking contents of requests with what we already have in the db
                page_insertions, page_updates = self.organize_needed_data(page_data, table_values, list(table.primary_key)[0].name, 
                    action_map)

                # Reached a page where we already have all tuples
                if len(need_insertion) == 0 and len(need_update) == 0 and \
                        backwards_activation:
                    self.logger.info("No more pages with unknown tuples, breaking from pagination.\n")
                    break

                need_insertion += page_insertions
                need_update += page_updates

            # Find last page so we can decrement from there
            if 'last' in response.links and last_page_number == -1:
                if platform == 'github':
                    last_page_number = int(response.links['last']['url'][-6:].split('=')[1])
                elif platform == 'gitlab':
                    last_page_number = int(response.links['last']['url'].split('&')[2].split('=')[1])

                if not forward_pagination and not backwards_activation:
                    page_number = last_page_number
                    backwards_activation = True

            self.logger.info("Analyzation of page {} of {} complete\n".format(page_number, 
                int(last_page_number) if last_page_number != -1 else "*last page not known*"))

            if (page_number <= 1 and not forward_pagination) or \
                    (page_number >= last_page_number and forward_pagination):
                self.logger.info("No more pages to check, breaking from pagination.\n")
                break

            page_number = page_number + 1 if forward_pagination else page_number - 1

        if forward_pagination:
            need_insertion, need_update = self.organize_needed_data(all_data, table_values, 
                list(table.primary_key)[0].name, action_map)

        return {
            'insert': need_insertion, 
            'update': need_update,
            'all': all_data
        }

    def paginate(self, url, duplicate_col_map, update_col_map, table, table_pkey, where_clause="", value_update_col_map={}, platform="github"):
        """ Paginate either backwards or forwards (depending on the value of the worker's
            finishing_task attribute) through all the GitHub or GitLab api endpoint pages.

        :param url: String, the url of the API endpoint we are paginating through, expects
            a curly brace string formatter within the string to format the Integer
            representing the page number that is wanted to be returned
        :param duplicate_col_map: Dictionary, maps the column names of the source data
            to the field names in our database for columns that should be checked for
            duplicates (if source data value == value in existing database row, then this
            element is a duplicate and would not need an insertion). Key is source data
            column name, value is database field name. Example: {'id': 'gh_issue_id'}
        :param update_col_map: Dictionary, maps the column names of the source data
            to the field names in our database for columns that should be checked for
            updates (if source data value != value in existing database row, then an
            update is needed). Key is source data column name, value is database field name.
            Example: {'id': 'gh_issue_id'}
        :param table: String, the name of the table that holds the values to check for
            duplicates/updates against
        :param table_pkey: String, the field name of the primary key of the table in
            the database that we are getting the values for to cross-reference to check
            for duplicates.
        :param where_clause: String, optional where clause to filter the values
            that are queried when preparing the values that will be cross-referenced
            for duplicates/updates
        :param value_update_col_map: Dictionary, sometimes we add a new field to a table,
            and we want to trigger an update of that row in the database even if all of the
            data values are the same and would not need an update ordinarily. Checking for
            a specific existing value in the database field allows us to do this. The key is the
            name of the field in the database we are checking for a specific value to trigger
            an update, the value is the value we are checking for equality to trigger an update.
            Example: {'cntrb_id': None}
        :return: List of dictionaries, all data points from the pages of the specified API endpoint
            each with a 'flag' key-value pair representing the required action to take with that
            data point (i.e. 'need_insertion', 'need_update', 'none')
        """

        update_keys = list(update_col_map.keys()) if update_col_map else []
        update_keys += list(value_update_col_map.keys()) if value_update_col_map else []
        cols_to_query = list(duplicate_col_map.keys()) + update_keys + [table_pkey]
        table_values = self.get_table_values(cols_to_query, [table], where_clause)

        i = 1
        multiple_pages = False
        tuples = []
        while True:
            num_attempts = 0
            success = False
            while num_attempts < 3:
                self.logger.info(f'Hitting endpoint: {url.format(i)}...\n')
                r = requests.get(url=url.format(i), headers=self.headers)

                self.update_rate_limit(r, platform=platform)
                if 'last' not in r.links:
                    last_page = None
                else:
                    if platform == "github":
                        last_page = r.links['last']['url'][-6:].split('=')[1]
                    elif platform == "gitlab":
                        last_page =  r.links['last']['url'].split('&')[2].split("=")[1]
                    self.logger.info("Analyzing page {} of {}\n".format(i, int(last_page) + 1 if last_page is not None else '*last page not known*'))

                try:
                    j = r.json()
                except:
                    j = json.loads(json.dumps(r.text))

                if type(j) != dict and type(j) != str:
                    success = True
                    break
                elif type(j) == dict:
                    self.logger.info("Request returned a dict: {}\n".format(j))
                    if j['message'] == 'Not Found':
                        self.logger.warning("Github repo was not found or does not exist for endpoint: {}\n".format(url))
                        break
                    if j['message'] == 'You have triggered an abuse detection mechanism. Please wait a few minutes before you try again.':
                        num_attempts -= 1
                        self.logger.info("rate limit update code goes here")
                        self.update_rate_limit(r, temporarily_disable=True,platform=platform)
                    if j['message'] == 'Bad credentials':
                        self.logger.info("rate limit update code goes here")
                        self.update_rate_limit(r, bad_credentials=True, platform=platform)
                elif type(j) == str:
                    self.logger.info(f'J was string: {j}\n')
                    if '<!DOCTYPE html>' in j:
                        self.logger.info('HTML was returned, trying again...\n')
                    elif len(j) == 0:
                        self.logger.warning('Empty string, trying again...\n')
                    else:
                        try:
                            j = json.loads(j)
                            success = True
                            break
                        except:
                            pass
                num_attempts += 1
            if not success:
                break

            # Find last page so we can decrement from there
            if 'last' in r.links and not multiple_pages and not self.finishing_task:
                if platform == "github":
                    param = r.links['last']['url'][-6:]
                    i = int(param.split('=')[1]) + 1
                elif platform == "gitlab":
                    i = int(r.links['last']['url'].split('&')[2].split("=")[1]) + 1
                self.logger.info("Multiple pages of request, last page is " + str(i - 1) + "\n")
                multiple_pages = True
            elif not multiple_pages and not self.finishing_task:
                self.logger.info("Only 1 page of request\n")
            elif self.finishing_task:
                self.logger.info("Finishing a previous task, paginating forwards ..."
                    " excess rate limit requests will be made\n")

            if len(j) == 0:
                self.logger.info("Response was empty, breaking from pagination.\n")
                break

            # Checking contents of requests with what we already have in the db
            j = self.assign_tuple_action(j, table_values, update_col_map, duplicate_col_map, table_pkey, value_update_col_map)

            if not j:
                self.logger.error("Assigning tuple action failed, moving to next page.\n")
                i = i + 1 if self.finishing_task else i - 1
                continue
            try:
                to_add = [obj for obj in j if obj not in tuples and (obj['flag'] != 'none')]
            except Exception as e:
                self.logger.error("Failure accessing data of page: {}. Moving to next page.\n".format(e))
                i = i + 1 if self.finishing_task else i - 1
                continue
            if len(to_add) == 0 and multiple_pages and 'last' in r.links:
                self.logger.info("{}".format(r.links['last']))
                if platform == "github":
                    page_number = int(r.links['last']['url'][-6:].split('=')[1])
                elif platform == "gitlab":
                    page_number = int(r.links['last']['url'].split('&')[2].split("=")[1])
                if i - 1 != page_number:
                    self.logger.info("No more pages with unknown tuples, breaking from pagination.\n")
                    break

            tuples += to_add

            i = i + 1 if self.finishing_task else i - 1

            # Since we already wouldve checked the first page... break
            if (i == 1 and multiple_pages and not self.finishing_task) or i < 1 or len(j) == 0:
                self.logger.info("No more pages to check, breaking from pagination.\n")
                break

        return tuples

    def query_github_contributors(self, entry_info, repo_id):

        """ Data collection function
        Query the GitHub API for contributors
        """
        self.logger.info(f"Querying contributors with given entry info: {entry_info}\n")

        github_url = entry_info['given']['github_url'] if 'github_url' in entry_info['given'] else entry_info['given']['git_url']

        # Extract owner/repo from the url for the endpoint
        owner, name = self.get_owner_repo(github_url)

        # Set the base of the url and place to hold contributors to insert
        contributors_url = (f"https://api.github.com/repos/{owner}/{name}/" + 
            "contributors?per_page=100&page={}")

        # Get contributors that we already have stored
        #   Set our duplicate and update column map keys (something other than PK) to
        #   check dupicates/needed column updates with
        table = 'contributors'
        table_pkey = 'cntrb_id'
        update_col_map = {'cntrb_email': 'email'}
        duplicate_col_map = {'cntrb_login': 'login'}

        #list to hold contributors needing insertion or update
        contributors = self.paginate(contributors_url, duplicate_col_map, update_col_map, table, table_pkey)

        self.logger.info("Count of contributors needing insertion: " + str(len(contributors)) + "\n")

        for repo_contributor in contributors:
            try:
                # Need to hit this single contributor endpoint to get extra data including...
                #   `created at`
                #   i think that's it
                cntrb_url = ("https://api.github.com/users/" + repo_contributor['login'])
                self.logger.info("Hitting endpoint: " + cntrb_url + " ...\n")
                r = requests.get(url=cntrb_url, headers=self.headers)
                self.update_gh_rate_limit(r)
                contributor = r.json()

                company = None
                location = None
                email = None
                if 'company' in contributor:
                    company = contributor['company']
                if 'location' in contributor:
                    location = contributor['location']
                if 'email' in contributor:
                    email = contributor['email']
                    canonical_email = contributor['email']

                cntrb = {
                    "cntrb_login": contributor['login'],
                    "cntrb_created_at": contributor['created_at'],
                    "cntrb_email": email,
                    "cntrb_company": company,
                    "cntrb_location": location,
                    # "cntrb_type": , dont have a use for this as of now ... let it default to null
                    "cntrb_canonical": canonical_email,
                    "gh_user_id": contributor['id'],
                    "gh_login": contributor['login'],
                    "gh_url": contributor['url'],
                    "gh_html_url": contributor['html_url'],
                    "gh_node_id": contributor['node_id'],
                    "gh_avatar_url": contributor['avatar_url'],
                    "gh_gravatar_id": contributor['gravatar_id'],
                    "gh_followers_url": contributor['followers_url'],
                    "gh_following_url": contributor['following_url'],
                    "gh_gists_url": contributor['gists_url'],
                    "gh_starred_url": contributor['starred_url'],
                    "gh_subscriptions_url": contributor['subscriptions_url'],
                    "gh_organizations_url": contributor['organizations_url'],
                    "gh_repos_url": contributor['repos_url'],
                    "gh_events_url": contributor['events_url'],
                    "gh_received_events_url": contributor['received_events_url'],
                    "gh_type": contributor['type'],
                    "gh_site_admin": contributor['site_admin'],
                    "tool_source": self.tool_source,
                    "tool_version": self.tool_version,
                    "data_source": self.data_source
                }

                # Commit insertion to table
                if repo_contributor['flag'] == 'need_update':
                    result = self.db.execute(self.contributors_table.update().where(
                        self.worker_history_table.c.cntrb_email==email).values(cntrb))
                    self.logger.info("Updated tuple in the contributors table with existing email: {}".format(email))
                    self.cntrb_id_inc = repo_contributor['pkey']
                elif repo_contributor['flag'] == 'need_insertion':
                    result = self.db.execute(self.contributors_table.insert().values(cntrb))
                    self.logger.info("Primary key inserted into the contributors table: {}".format(result.inserted_primary_key))
                    self.results_counter += 1

                    self.logger.info("Inserted contributor: " + contributor['login'] + "\n")

                    # Increment our global track of the cntrb id for the possibility of it being used as a FK
                    self.cntrb_id_inc = int(result.inserted_primary_key[0])

            except Exception as e:
                self.logger.error("Caught exception: {}".format(e))
                self.logger.error("Cascading Contributor Anomalie from missing repo contributor data: {} ...\n".format(cntrb_url))
                continue


    def query_github_contributors_bulk(self, entry_info, repo_id):

        """ Data collection function
        Query the GitHub API for contributors
        """
        self.logger.info(f"Querying contributors with given entry info: {entry_info}\n")

        github_url = entry_info['given']['github_url'] if 'github_url' in entry_info['given'] else entry_info['given']['git_url']

        owner, name = self.get_owner_repo(github_url)

        contributors_url = (f"https://api.github.com/repos/{owner}/{name}/" + 
            "contributors?per_page=100&page={}")

        action_map = {
            'insert': {
                'source': ['login'],
                'augur': ['cntrb_login']
            },
            'update': {
                'source': ['email'],
                'augur': ['cntrb_email']
            }
        }

        source_contributors = self.paginate_endpoint(contributors_url, action_map=action_map, 
            table=self.contributors_table)

        contributors_insert_result = []
                
        for repo_contributor in source_contributors['insert']:
            # Need to hit this single contributor endpoint to get extra data
            cntrb_url = (f"https://api.github.com/users/{repo_contributor['login']}")
            self.logger.info(f"Hitting endpoint: {cntrb_url} ...\n")
            r = requests.get(url=cntrb_url, headers=self.headers)
            self.update_gh_rate_limit(r)
            contributor = r.json()

            contributors_insert_result.append({
                'cntrb_login': contributor['login'],
                'cntrb_created_at': contributor['created_at'],
                'cntrb_email': contributor['email'] if 'email' in contributor else None,
                'cntrb_company': contributor['company'] if 'company' in contributor else None,
                'cntrb_location': contributor['location'] if 'location' in contributor else None,
                'cntrb_canonical': contributor['email'] if 'email' in contributor else None,
                'gh_user_id': contributor['id'],
                'gh_login': contributor['login'],
                'gh_url': contributor['url'],
                'gh_html_url': contributor['html_url'],
                'gh_node_id': contributor['node_id'],
                'gh_avatar_url': contributor['avatar_url'],
                'gh_gravatar_id': contributor['gravatar_id'],
                'gh_followers_url': contributor['followers_url'],
                'gh_following_url': contributor['following_url'],
                'gh_gists_url': contributor['gists_url'],
                'gh_starred_url': contributor['starred_url'],
                'gh_subscriptions_url': contributor['subscriptions_url'],
                'gh_organizations_url': contributor['organizations_url'],
                'gh_repos_url': contributor['repos_url'],
                'gh_events_url': contributor['events_url'],
                'gh_received_events_url': contributor['received_events_url'],
                'gh_type': contributor['type'],
                'gh_site_admin': contributor['site_admin'],
                'tool_source': self.tool_source,
                'tool_version': self.tool_version,
                'data_source': self.data_source
            })

        contributors_insert_result, contributors_update_result = self.bulk_insert(self.contributors_table, 
            update=source_contributors['update'], unique_columns=action_map['insert']['augur'], 
            insert=contributors_insert, update_columns=action_map['update']['augur'])

    def query_gitlab_contribtutors(self, entry_info, repo_id):

        gitlab_url = entry_info['given']['gitlab_url'] if 'gitlab_url' in entry_info['given'] else entry_info['given']['git_url']

        self.logger.info("Querying contributors with given entry info: " + str(entry_info) + "\n")

        path = urlparse(gitlab_url)
        split = path[2].split('/')

        owner = split[1]
        name = split[2]

        # Handles git url case by removing the extension
        if ".git" in name:
            name = name[:-4]

        url_encoded_format = quote(owner + '/' + name, safe='')

        table = 'contributors'
        table_pkey = 'cntrb_id'
        update_col_map = {'cntrb_email': 'email'}
        duplicate_col_map = {'cntrb_login': 'email'}

        # list to hold contributors needing insertion or update
        contributors = self.paginate("https://gitlab.com/api/v4/projects/" + url_encoded_format + "/repository/contributors?per_page=100&page={}", duplicate_col_map, update_col_map, table, table_pkey, platform='gitlab')

        for repo_contributor in contributors:
            try:
                cntrb_compressed_url = ("https://gitlab.com/api/v4/users?search=" + repo_contributor['email'])
                self.logger.info("Hitting endpoint: " + cntrb_compressed_url + " ...\n")
                r = requests.get(url=cntrb_compressed_url, headers=self.headers)
                contributor_compressed = r.json()

                email = repo_contributor['email']
                self.logger.info(contributor_compressed)
                if len(contributor_compressed) == 0 or type(contributor_compressed) is dict or "id" not in contributor_compressed[0]:
                    continue

                self.logger.info("Fetching for user: " + str(contributor_compressed[0]["id"]))

                cntrb_url = ("https://gitlab.com/api/v4/users/" + str(contributor_compressed[0]["id"]))
                self.logger.info("Hitting end point to get complete contributor info now: " + cntrb_url + "...\n")
                r = requests.get(url=cntrb_url, headers=self.headers)
                contributor = r.json()

                cntrb = {
                    "cntrb_login": contributor.get('username', None),
                    "cntrb_created_at": contributor.get('created_at', None),
                    "cntrb_email": email,
                    "cntrb_company": contributor.get('organization', None),
                    "cntrb_location": contributor.get('location', None),
                    # "cntrb_type": , dont have a use for this as of now ... let it default to null
                    "cntrb_canonical": contributor.get('public_email', None),
                    "gh_user_id": contributor.get('id', None),
                    "gh_login": contributor.get('username', None),
                    "gh_url": contributor.get('web_url', None),
                    "gh_html_url": contributor.get('web_url', None),
                    "gh_node_id": None,
                    "gh_avatar_url": contributor.get('avatar_url', None),
                    "gh_gravatar_id": None,
                    "gh_followers_url": None,
                    "gh_following_url": None,
                    "gh_gists_url": None,
                    "gh_starred_url": None,
                    "gh_subscriptions_url": None,
                    "gh_organizations_url": None,
                    "gh_repos_url": None,
                    "gh_events_url": None,
                    "gh_received_events_url": None,
                    "gh_type": None,
                    "gh_site_admin": None,
                    "tool_source": self.tool_source,
                    "tool_version": self.tool_version,
                    "data_source": self.data_source
                }

                # Commit insertion to table
                if repo_contributor['flag'] == 'need_update':
                    result = self.db.execute(self.contributors_table.update().where(
                        self.worker_history_table.c.cntrb_email == email).values(cntrb))
                    self.logger.info("Updated tuple in the contributors table with existing email: {}".format(email))
                    self.cntrb_id_inc = repo_contributor['pkey']
                elif repo_contributor['flag'] == 'need_insertion':
                    result = self.db.execute(self.contributors_table.insert().values(cntrb))
                    self.logger.info("Primary key inserted into the contributors table: {}".format(result.inserted_primary_key))
                    self.results_counter += 1

                    self.logger.info("Inserted contributor: " + contributor['username'] + "\n")

                    # Increment our global track of the cntrb id for the possibility of it being used as a FK
                    self.cntrb_id_inc = int(result.inserted_primary_key[0])

            except Exception as e:
                self.logger.info("Caught exception: {}".format(e))
                self.logger.info("Cascading Contributor Anomalie from missing repo contributor data: {} ...\n".format(cntrb_url))
                continue

    def record_model_process(self, repo_id, model):

        task_history = {
            "repo_id": repo_id,
            "worker": self.config['id'],
            "job_model": model,
            "oauth_id": self.oauths[0]['oauth_id'],
            "timestamp": datetime.datetime.now(),
            "status": "Stopped",
            "total_results": self.results_counter
        }
        if self.finishing_task:
            result = self.helper_db.execute(self.worker_history_table.update().where(
                self.worker_history_table.c.history_id==self.history_id).values(task_history))
            self.history_id += 1
        else:
            result = self.helper_db.execute(self.worker_history_table.insert().values(task_history))
            self.logger.info("Record incomplete history tuple: {}\n".format(result.inserted_primary_key))
            self.history_id = int(result.inserted_primary_key[0])

        self.collection_start_time = time.time()

    def register_task_completion(self, task, repo_id, model):

        self.logger.info(f"Worker completed this task in {self.collection_start_time - time.time()} seconds.\n")

        # Task to send back to broker
        task_completed = {
            'worker_id': self.config['id'],
            'job_type': "MAINTAIN",
            'repo_id': repo_id,
            'job_model': model
        }
        key = 'github_url' if 'github_url' in task['given'] else 'git_url' if 'git_url' in task['given'] else \
            'gitlab_url' if 'gitlab_url' in task['given'] else 'INVALID_GIVEN'
        task_completed[key] = task['given']['github_url'] if 'github_url' in task['given'] else task['given']['git_url'] \
            if 'git_url' in task['given'] else task['given']['gitlab_url'] if 'gitlab_url' in task['given'] else 'INVALID_GIVEN'
        if key == 'INVALID_GIVEN':
            self.register_task_failure(task, repo_id, "INVALID_GIVEN: Not a github/gitlab/git url.")
            return

        # Add to history table
        task_history = {
            'repo_id': repo_id,
            'worker': self.config['id'],
            'job_model': model,
            'oauth_id': self.oauths[0]['oauth_id'],
            'timestamp': datetime.datetime.now(),
            'status': "Success",
            'total_results': self.results_counter
        }
        self.helper_db.execute(self.worker_history_table.update().where(
            self.worker_history_table.c.history_id==self.history_id).values(task_history))

        self.logger.info(f"Recorded job completion for: {task_completed}\n")

        # Update job process table
        updated_job = {
            'since_id_str': repo_id,
            'last_count': self.results_counter,
            'last_run': datetime.datetime.now(),
            'analysis_state': 0
        }
        self.helper_db.execute(self.worker_job_table.update().where(
            self.worker_job_table.c.job_model==model).values(updated_job))
        self.logger.info(f"Updated job process for model: {model}\n")

        if self.config['offline_mode'] is False:
            
            # Notify broker of completion
            self.logger.info(f"Telling broker we completed task: {task_completed}\n") 
            self.logger.info(f"This task inserted: {self.results_counter + self.insert_counter} tuples " +
                f"and updated {self.update_counter} tuples.\n")

            requests.post('http://{}:{}/api/unstable/completed_task'.format(
                self.config['host_broker'],self.config['port_broker']), json=task_completed)

        # Reset results counter for next task
        self.results_counter = 0
        self.insert_counter = 0
        self.update_counter = 0

    def register_task_failure(self, task, repo_id, e):

        self.logger.error(f"Worker ran into an error for task: {task}\n")
        self.logger.error(f"Worker was processing this task for {self.collection_start_time - time.time()} seconds.\n")
        self.logger.error("Printing traceback...\n")
        self.logger.error(e)
        tb = traceback.format_exc()
        self.logger.error(tb)

        self.logger.info(f'This task inserted {self.results_counter} tuples before failure.\n')
        self.logger.info("Notifying broker and logging task failure in database...\n")
        key = 'github_url' if 'github_url' in task['given'] else 'git_url' if 'git_url' in task['given'] else \
            'gitlab_url' if 'gitlab_url' in task['given'] else 'INVALID_GIVEN'
        url = task['given'][key]

        """ Query all repos with repo url of given task """
        repoUrlSQL = s.sql.text("""
            SELECT min(repo_id) as repo_id FROM repo WHERE repo_git = '{}'
            """.format(url))
        repo_id = int(pd.read_sql(repoUrlSQL, self.db, params={}).iloc[0]['repo_id'])

        task['worker_id'] = self.config['id']
        try:
            requests.post("http://{}:{}/api/unstable/task_error".format(
                self.config['host_broker'],self.config['port_broker']), json=task)
        except requests.exceptions.ConnectionError:
            self.logger.error('Could not send task failure message to the broker\n')
            self.logger.error(e)
        except Exception:
            self.logger.error('An error occured while informing broker about task failure\n')
            self.logger.error(e)

        # Add to history table
        task_history = {
            "repo_id": repo_id,
            "worker": self.config['id'],
            "job_model": task['models'][0],
            "oauth_id": self.oauths[0]['oauth_id'],
            "timestamp": datetime.datetime.now(),
            "status": "Error",
            "total_results": self.results_counter
        }
        self.helper_db.execute(self.worker_history_table.update().where(self.worker_history_table.c.history_id==self.history_id).values(task_history))

        self.logger.error("Recorded job error in the history table for: " + str(task) + "\n")

        # Update job process table
        updated_job = {
            "since_id_str": repo_id,
            "last_count": self.results_counter,
            "last_run": datetime.datetime.now(),
            "analysis_state": 0
        }
        self.helper_db.execute(self.worker_job_table.update().where(self.worker_job_table.c.job_model==task['models'][0]).values(updated_job))
        self.logger.info("Updated job process for model: " + task['models'][0] + "\n")

        # Reset results counter for next task
        self.results_counter = 0

    def get_relevant_columns(self, table, action_map={}):
        columns = copy.deepcopy(action_map['update']['augur']) if 'update' in action_map else []
        columns += action_map['value_update']['augur'] if 'value_update' in action_map else []
        columns += action_map['insert']['augur'] if 'insert' in action_map else []
        return [table.c[column] for column in
            columns + [list(table.primary_key)[0].name]]

    def retrieve_tuple(self, key_values, tables):
        table_str = tables[0]
        del tables[0]

        key_values_items = list(key_values.items())
        for col, value in [key_values_items[0]]:
            where_str = col + " = '" + value + "'"
        del key_values_items[0]

        for col, value in key_values_items:
            where_str += ' AND ' + col + " = '" + value + "'"
        for table in tables:
            table_str += ", " + table

        retrieveTupleSQL = s.sql.text("""
            SELECT * FROM {} WHERE {}
            """.format(table_str, where_str))
        values = json.loads(pd.read_sql(retrieveTupleSQL, self.db, params={}).to_json(orient="records"))
        return values
