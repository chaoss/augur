# Copyright 2016-2018 Brian Warner
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier:  Apache-2.0

# Git repo maintenance
#
# This script is responsible for cloning new repos and keeping existing repos up
# to date. It can be run as often as you want (and will detect when it's
# already running, so as not to spawn parallel processes), but once or twice per
# day should be more than sufficient. Each time it runs, it updates the repo
# and checks for any parents of HEAD that aren't already accounted for in the
# repos. It also rebuilds analysis data, checks any changed affiliations and
# aliases, and caches data for display.
import sys
import platform
import imp
import time
import datetime
import html.parser
import subprocess
import os
import getopt
import xlsxwriter
import configparser
import psycopg2
import json
import logging
import random
from urllib.parse import urlparse
import sqlalchemy as s
from sqlalchemy.exc import OperationalError
from psycopg2.errors import DeadlockDetected

from augur.tasks.github.util.github_task_session import *
from augur.application.logs import AugurLogger
from augur.application.config import AugurConfig
from logging import Logger

logger = logging.getLogger(__name__)

def get_database_args_from_env():

    db_str = os.getenv("AUGUR_DB")
    try:
        db_json_file_location = os.getcwd() + "/db.config.json"
    except FileNotFoundError:
        logger.error("\n\nPlease run augur commands in the root directory\n\n")
        sys.exit()

    db_json_exists = os.path.exists(db_json_file_location)

    if not db_str and not db_json_exists:

        logger.error("ERROR no way to get connection to the database. \n\t\t\t\t\t\t    There is no db.config.json and the AUGUR_DB environment variable is not set\n\t\t\t\t\t\t    Please run make install or set the AUGUR_DB environment then run make install")
        sys.exit()

    credentials = {}
    if db_str:
        parsedArgs = urlparse(db_str)

        credentials['db_user'] = parsedArgs.username#read_config('Database', 'user', 'AUGUR_DB_USER', 'augur')
        credentials['db_pass'] = parsedArgs.password#read_config('Database', 'password', 'AUGUR_DB_PASSWORD', 'augur')
        credentials['db_name'] = parsedArgs.path.replace('/','')#read_config('Database', 'name', 'AUGUR_DB_NAME', 'augur')
        credentials['db_host'] = parsedArgs.hostname#read_config('Database', 'host', 'AUGUR_DB_HOST', 'localhost')
        credentials['db_port'] = parsedArgs.port#read_config('Database', 'port', 'AUGUR_DB_PORT', 5432)
    else:
        with open("db.config.json", 'r') as f:
            db_config = json.load(f)

        credentials['db_user'] = db_config["user"]#read_config('Database', 'user', 'AUGUR_DB_USER', 'augur')
        credentials['db_pass'] = db_config["password"]#read_config('Database', 'password', 'AUGUR_DB_PASSWORD', 'augur')
        credentials['db_name'] = db_config["database_name"]#read_config('Database', 'name', 'AUGUR_DB_NAME', 'augur')
        credentials['db_host'] = db_config["host"]#read_config('Database', 'host', 'AUGUR_DB_HOST', 'localhost')
        credentials['db_port'] = db_config["port"]#read_config('Database', 'port', 'AUGUR_DB_PORT', 5432)
    #print(credentials)
    return credentials

class FacadeSession(GithubTaskSession):
    """ORM session used in facade tasks.

        This class adds the various attributes needed for legacy facade as well as a modified version of the legacy FacadeConfig class.
        This is mainly for compatibility with older functions from legacy facade.

    Attributes:
        repos_processed (int): git repositories processed
        limited_run (int): value that determines whether legacy facade is only doing a portion of its full run of commit analysis or not. By default all steps are run but if any options in particular are specified then only those are ran.
        delete_marked_repos (int): toggle that determines whether to delete git cloned git directories when they are marked for deletion
        pull_repos (int): toggles whether to update existing repos in the facade directory
        clone_repos (int): toggles whether to run 'git clone' on repos that haven't been cloned yet.
        check_updates (int): toggles whether to check if any repos are marked for update
        force_updates (int): force all repos to have 'git pull' run on them
        run_analysis (int): toggles analysis of repos in a limited run
        force_analysis (int): forces all repos to have their commits analyzed by legacy facade.
        nuke_stored_affiliations (int): toggles nuking facade affliations
        fix_affiliations (int): toggles filling empty affilations
        force_invalidate_caches (int): toggles whether to clear facade's backend caches
        rebuild_caches (int): toggles whether to rebuild unknown affiliation and web caches
        multithreaded (int): toggles whether to allow the facade task to execute subtasks in parallel
        create_xlsx_summary_files (int): toggles whether to create excel summary files
    """
    def __init__(self,logger: Logger):

        from augur.tasks.init.celery_app import engine
        #self.cfg = FacadeConfig(logger)
        self.repos_processed = 0
        super().__init__(logger=logger, engine=engine)
        # Figure out what we need to do
        
        worker_options = AugurConfig(logger, self).get_section("Facade")

        self.limited_run = worker_options["limited_run"]
        self.delete_marked_repos = worker_options["delete_marked_repos"]
        self.pull_repos = worker_options["pull_repos"]
        #self.clone_repos = worker_options["clone_repos"]
        self.check_updates = worker_options["check_updates"]
        #self.force_updates = worker_options["force_updates"]
        self.run_analysis = worker_options["run_analysis"]
        #self.force_analysis = worker_options["force_analysis"]
        self.run_facade_contributors = worker_options["run_facade_contributors"]
        self.nuke_stored_affiliations = worker_options["nuke_stored_affiliations"]
        self.fix_affiliations = worker_options["fix_affiliations"]
        self.force_invalidate_caches = worker_options["force_invalidate_caches"]
        self.rebuild_caches = worker_options["rebuild_caches"]
        self.multithreaded = worker_options["multithreaded"]
        self.create_xlsx_summary_files = worker_options["create_xlsx_summary_files"]

        self.tool_source = "Facade"
        self.data_source = "Git Log"
        self.tool_version = "1.4.4"

        # Get the location of the directory where git repos are stored
        if 'repo_directory' in worker_options:
            self.repo_base_directory = worker_options['repo_directory']
        else:
            self.repo_base_directory = None

        # Determine if it's safe to start the script
        current_status = self.get_setting('utility_status')

        if len(self.repo_base_directory) == 0:
            self.cfg.log_activity('Error','No base directory. It is unsafe to continue.')
            raise Exception('Failed: No base directory')

    def get_setting(self,setting):
        #Get a setting from the db

        query = s.sql.text("""SELECT value FROM settings WHERE setting=:settingParam ORDER BY
            last_modified DESC LIMIT 1""").bindparams(settingParam=setting)
        
        result = self.execute_sql(query).fetchone()
        print(result)
        return result[0]
        

    def update_status(self, status):
        query = s.sql.text("""UPDATE settings SET value=:statusParam WHERE setting='utility_status'
            """).bindparams(statusParam=status)
        
        self.execute_sql(query)

    def log_activity(self, level, status):
        # Log an activity based upon urgency and user's preference.  If the log level is
        # "Debug", then just print it and don't save it in the database.
        log_options = ('Error','Quiet','Info','Verbose','Debug')
        self.logger.info(f"* {status}\n")

        #Return if only debug 
        if level == 'Debug':
            return
        
        #Else write to database
        query = s.sql.text("""INSERT INTO utility_log (level,status) VALUES (:levelParam,:statusParam)
            """).bindparams(levelParam=level,statusParam=status)

        try:
            self.execute_sql(query)
        except Exception as e:
            self.logger.error(f"Error encountered: {e}")
            raise e
    def update_repo_log(self,repos_id,status):
        self.logger.info(f"{status} {repos_id}")

        log_message = s.sql.text("""INSERT INTO repos_fetch_log (repos_id,status) 
            VALUES (:repo_id,:repo_status)""").bindparams(repo_id=repos_id,repo_status=status)
        
        try:
            self.execute_sql(log_message)
        except:
            pass
    def insert_or_update_data(self, query, **bind_args)-> None:
        """Provide deadlock detection for postgres updates, inserts, and deletions for facade.

        Returns:
            A page of data from the Github API at the specified url
        """

        attempts = 0
        sleep_time_list = [x for x in range(1,11)]
        deadlock_detected = False
        # if there is no data to return then it executes the insert the returns nothing

        while attempts < 10:
            try:
                if bind_args:
                    #self.cfg.cursor.execute(query, params)
                    self.execute_sql(query.bindparams(**bind_args))
                else:
                    self.execute_sql(query)
                break
            except OperationalError as e:
                # print(str(e).split("Process")[1].split(";")[0])
                if isinstance(e.orig, DeadlockDetected):
                    deadlock_detected = True
                    sleep_time = random.choice(sleep_time_list)
                    self.logger.debug(f"Deadlock detected on query {query}...trying again in {round(sleep_time)} seconds")
                    time.sleep(sleep_time)

                    attempts += 1
                    continue
                else:
                    raise OperationalError(f"An OperationalError other than DeadlockDetected occurred: {e}") 

        else:
            self.logger.error(f"Unable to insert data in 10 attempts")
            return

        if deadlock_detected is True:
            self.logger.error(f"Made it through even though Deadlock was detected")
                    
            return
    def inc_repos_processed(self):
        self.repos_processed += 1

"""
class FacadeConfig:
    \"""Legacy facade config that holds facade's database functionality
        
        This is mainly for compatibility with older functions from legacy facade.

        Initializes database when it encounters a database exception

    Attributes:
        repos_processed (int): Counter for how many repos have been analyzed
        cursor (psycopg2.extensions.cursor): database cursor for legacy facade.
        logger (Logger): logger object inherited from the session object
        db (psycopg2.extensions.connection): database connection object for legacy facade.
        tool_source (str): String marking the source of data as from facade.
        data_source (str): String indicating that facade gets data from git
        tool_version (str): Facade version
        worker_options (dict): Config options for facade.
        log_level (str): Keyword indicating level of logging for legacy facade.
    \"""
    def __init__(self, logger: Logger):
        self.repos_processed = 0
        self.cursor = None
        self.logger = logger

        self.db = None
        
        #init db first thing 
        db_credentials = get_database_args_from_env()

        # Set up the database
        db_user = db_credentials["db_user"]
        db_pass = db_credentials["db_pass"]
        db_name = db_credentials["db_name"]
        db_host = db_credentials["db_host"]
        db_port = db_credentials["db_port"]
        db_user_people = db_user
        db_pass_people = db_pass
        db_name_people = db_name
        db_host_people = db_host
        db_port_people = db_port
        # Open a general-purpose connection
        db,cursor = self.database_connection(
            db_host,
            db_user,
            db_pass,
            db_name,
            db_port, False, False)

        #worker_options = read_config("Workers", "facade_worker", None, None)

        with DatabaseSession(logger) as session:
            config = AugurConfig(logger, session)
            worker_options = config.get_section("Facade")

        if 'repo_directory' in worker_options:
            self.repo_base_directory = worker_options['repo_directory']
        else:
            self.log_activity('Error',"Please specify a \'repo_directory\' parameter"
                " in your \'Workers\' -> \'facade_worker\' object in your config "
                "to the directory in which you want to clone repos. Exiting...")
            sys.exit(1)

        self.tool_source = '\'Facade \''
        self.tool_version = '\'1.3.0\''
        self.data_source = '\'Git Log\''

        self.worker_options = worker_options

        # Figure out how much we're going to log
        #logging.basicConfig(filename='worker_{}.log'.format(worker_options['port']), filemode='w', level=logging.INFO)
        self.log_level = None #self.get_setting('log_level')


    #### Database update functions ####

    def increment_db(self, version):

        # Helper function to increment the database number

        increment_db = ("INSERT INTO settings (setting,value) "
            "VALUES ('database_version',%s)")
        self.cursor.execute(increment_db, (version, ))
        db.commit()

        print("Database updated to version: %s" % version)

    def update_db(self, version):

        # This function should incrementally step any version of the database up to
        # the current schema. After executing the database operations, call
        # increment_db to bring it up to the version with which it is now compliant.

        print("Legacy Facade Block for DB UPDATE. No longer used. ")

        print("No further database updates.\n")

    def migrate_database_config(self):

    # Since we're changing the way we store database credentials, we need a way to
    # transparently migrate anybody who was using the old file. Someday after a long
    # while this can disappear.

        try:
            # If the old database config was found, write a new config
            imp.find_module('db')

            db_config = configparser.ConfigParser()

            from db import db_user,db_pass,db_name,db_host
            from db import db_user_people,db_pass_people,db_name_people,db_host_people

            db_config.add_section('main_database')
            db_config.set('main_database','user',db_user)
            db_config.set('main_database','pass',db_pass)
            db_config.set('main_database','name',db_name)
            db_config.set('main_database','host',db_host)

            db_config.add_section('people_database')
            db_config.set('people_database','user',db_user_people)
            db_config.set('people_database','pass',db_pass_people)
            db_config.set('people_database','name',db_name_people)
            db_config.set('people_database','host',db_host_people)

            with open('db.cfg','w') as db_file:
                db_config.write(db_file)

            print("Migrated old style config file to new.")
        except:
            # If nothing is found, the user probably hasn't run setup yet.
            sys.exit("Can't find database config. Have you run setup.py?")

        try:
            os.remove('db.py')
            os.remove('db.pyc')
            print("Removed unneeded config files")
        except:
            print("Attempted to remove unneeded config files")

        return db_user,db_pass,db_name,db_host,db_user_people,db_pass_people,db_name_people,db_host_people

    #### Global helper functions ####

    def database_connection(self, db_host,db_user,db_pass,db_name, db_port, people, multi_threaded_connection):

    # Return a database connection based upon which interpreter we're using. CPython
    # can use any database connection, although MySQLdb is preferred over pymysql
    # for performance reasons. However, PyPy can't use MySQLdb at this point,
    # instead requiring a pure python MySQL client. This function returns a database
    # connection that should provide maximum performance depending upon the
    # interpreter in use.

    ##TODO: Postgres connections as we make them ARE threadsafe. We *could* refactor this accordingly: https://www.psycopg.org/docs/connection.html #noturgent


        # if platform.python_implementation() == 'PyPy':
        db_schema = 'augur_data'
        db = psycopg2.connect(
            host = db_host,
            user = db_user,
            password = db_pass,
            database = db_name,
            # charset = 'utf8mb4',
            port = db_port,
            options=f'-c search_path={db_schema}',
            connect_timeout = 31536000,)

        cursor = db.cursor()#pymysql.cursors.DictCursor)


        self.cursor = cursor
        self.db = db

        # Figure out how much we're going to log
        #self.log_level = self.get_setting('log_level')
        #Not getting debug logging for some reason.
        self.log_level = 'Debug'
        return db, cursor

    def get_setting(self, setting):

    # Get a setting from the database

        query = (\"""SELECT value FROM settings WHERE setting=%s ORDER BY
            last_modified DESC LIMIT 1\""")
        self.cursor.execute(query, (setting, ))
        # print(type(self.cursor.fetchone()))
        return self.cursor.fetchone()[0]#["value"]

    def update_status(self, status):

    # Update the status displayed in the UI

        query = ("UPDATE settings SET value=%s WHERE setting='utility_status'")
        self.cursor.execute(query, (status, ))
        self.db.commit()

    def log_activity(self, level, status):

    # Log an activity based upon urgency and user's preference.  If the log level is
    # "Debug", then just print it and don't save it in the database.

        log_options = ('Error','Quiet','Info','Verbose','Debug')
        self.logger.info("* %s\n" % status)
        if self.log_level == 'Debug' and level == 'Debug':
            return

        #if log_options.index(level) <= log_options.index(self.log_level):
        query = ("INSERT INTO utility_log (level,status) VALUES (%s,%s)")
        try:
            self.cursor.execute(query, (level, status))
            self.db.commit()
        except Exception as e:
            self.logger.info('Error encountered: {}\n'.format(e))

            db_credentials = get_database_args_from_env()

            # Set up the database
            db_user = db_credentials["db_user"]
            db_pass = db_credentials["db_pass"]
            db_name = db_credentials["db_name"]
            db_host = db_credentials["db_host"]
            db_port = db_credentials["db_port"]
            db_user_people = db_user
            db_pass_people = db_pass
            db_name_people = db_name
            db_host_people = db_host
            db_port_people = db_port
            # Open a general-purpose connection
            db,cursor = self.database_connection(
                db_host,
                db_user,
                db_pass,
                db_name,
                db_port, False, False)
            self.cursor.execute(query, (level, status))
            self.db.commit()




"""
