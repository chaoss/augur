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
import pymysql
import psycopg2
import json
import logging
logging.basicConfig(filename='worker.log', filemode='w', level=logging.INFO)

class Config:

    def __init__(self):
        self.upstream_db = 7
        self.cursor = None
        self.cursor_people = None

        # Figure out how much we're going to log
        self.log_level = None #self.get_setting('log_level')

        self.db = None
        self.db_people = None

        worker_options = self.read_config("Workers", "facade_worker", use_main_config=1)
        if 'repo_directory' in worker_options:
            self.repo_base_directory = worker_options['repo_directory']
        else:
            self.log_activity('Error',"Please specify a \'repo_directory\' parameter"
                " in your \'Workers\' -> \'facade_worker\' object in your config "
                "to the directory in which you want to clone repos. Exiting...")
            sys.exit(1)
        self.tool_source = '\'FacadeAugur\''
        self.tool_version = '\'0.0.1\''
        self.data_source = '\'git_repository\''

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

        print("Attempting database update")

        if version < 0:

            increment_db(0)

        if version < 1:
            # for commit f49b2f0e46b32997a72508bc83a6b1e834069588
            add_update_frequency = ("INSERT INTO settings (setting,value) "
                "VALUES ('update_frequency',24)")
            self.cursor.execute(add_update_frequency)
            self.db.commit

            increment_db(1)

        if version < 2:
            add_recache_to_projects = ("ALTER TABLE projects ADD COLUMN "
                "recache BOOL DEFAULT TRUE")
            self.cursor.execute(add_recache_to_projects)
            self.db.commit

            increment_db(2)

        if version < 3:
            add_results_setting = ("INSERT INTO settings (setting,value) "
                "VALUES ('results_visibility','show')")
            self.cursor.execute(add_results_setting)
            self.db.commit

            increment_db(3)

        if version < 4:
            add_working_commits_table = ("CREATE TABLE IF NOT EXISTS working_commits ("
                "repos_id INT UNSIGNED NOT NULL,"
                "working_commit VARCHAR(40))")

            self.cursor.execute(add_working_commits_table)
            self.db.commit

            # Make sure all working commits are processed

            get_working_commits = ("SELECT id,working_commit "
                "FROM repos WHERE working_commit > ''")

            self.cursor.execute(get_working_commits)

            working_commits = list(self.cursor)

            for commit in working_commits:
                trim_commit(commit['id'],commit['working_commit'])

            # Now it's safe to discard the (now unused) column

            remove_working_commit_column = ("ALTER TABLE repos DROP COLUMN "
                "working_commit")

            self.cursor.execute(remove_working_commit_column)
            self.db.commit

            increment_db(4)

        if version < 5:

            add_weekly_project_cache = ("CREATE TABLE IF NOT EXISTS project_weekly_cache ("
                "projects_id INT UNSIGNED NOT NULL,"
                "email VARCHAR(128) NOT NULL,"
                "affiliation VARCHAR(128),"
                "week TINYINT UNSIGNED NOT NULL,"
                "year SMALLINT UNSIGNED NOT NULL,"
                "added BIGINT UNSIGNED NOT NULL,"
                "removed BIGINT UNSIGNED NOT NULL,"
                "whitespace BIGINT UNSIGNED NOT NULL,"
                "files BIGINT UNSIGNED NOT NULL,"
                "patches BIGINT UNSIGNED NOT NULL,"
                "INDEX `projects_id,year,affiliation` (projects_id,year,affiliation),"
                "INDEX `projects_id,year,email` (projects_id,year,email),"
                "INDEX `projects_id,affiliation` (projects_id,affiliation),"
                "INDEX `projects_id,email` (projects_id,email))")

            self.cursor.execute(add_weekly_project_cache)
            self.db.commit

            add_weekly_repo_cache = ("CREATE TABLE IF NOT EXISTS repo_weekly_cache ("
                "repos_id INT UNSIGNED NOT NULL,"
                "email VARCHAR(128) NOT NULL,"
                "affiliation VARCHAR(128),"
                "week TINYINT UNSIGNED NOT NULL,"
                "year SMALLINT UNSIGNED NOT NULL,"
                "added BIGINT UNSIGNED NOT NULL,"
                "removed BIGINT UNSIGNED NOT NULL,"
                "whitespace BIGINT UNSIGNED NOT NULL,"
                "files BIGINT UNSIGNED NOT NULL,"
                "patches BIGINT UNSIGNED NOT NULL,"
                "INDEX `repos_id,year,affiliation` (repos_id,year,affiliation),"
                "INDEX `repos_id,year,email` (repos_id,year,email),"
                "INDEX `repos_id,affiliation` (repos_id,affiliation),"
                "INDEX `repos_id,email` (repos_id,email))")

            self.cursor.execute(add_weekly_repo_cache)
            self.db.commit

            increment_db(5)

        if version < 6:

            # As originally written, the UNIQUE wasn't working because it allowed
            # multiple NULL values in end_date.

            drop_special_tags_constraint = ("ALTER TABLE special_tags "
                "DROP INDEX `email,start_date,end_date,tag`")

            self.cursor.execute(drop_special_tags_constraint)
            self.db.commit

            add_unique_in_special_tags = ("ALTER TABLE special_tags "
                "ADD UNIQUE `email,start_date,tag` (email,start_date,tag)")

            self.cursor.execute(add_unique_in_special_tags)
            self.db.commit

            increment_db(6)

        if version < 7:

            # Using NULL for en unbounded nd_date in special_tags ended up being
            # difficult when doing certain types of reports. The logic is much
            # cleaner if we just use an end_date that is ridiculously far into the
            # future.

            remove_null_end_dates_in_special_tags = ("UPDATE special_tags "
                "SET end_date = '9999-12-31' WHERE end_date IS NULL")

            self.cursor.execute(remove_null_end_dates_in_special_tags)
            self.db.commit

            increment_db(7)

        print("No further database updates.\n")

    def read_config(self, section, name=None, environment_variable=None, default=None, config_file='augur.config.json', no_config_file=0, use_main_config=0):
        """
        Read a variable in specified section of the config file, unless provided an environment variable

        :param section: location of given variable
        :param name: name of variable
        """


        __config_bad = False
        if use_main_config == 0:
            __config_file_path = os.path.abspath(os.getenv('AUGUR_CONFIG_FILE', config_file))
        else:        
            __config_file_path = os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd())) + '/augur.config.json')

        __config_location = os.path.dirname(__config_file_path)
        __export_env = os.getenv('AUGUR_ENV_EXPORT', '0') == '1'
        __default_config = { 'Database': {"host": "nekocase.augurlabs.io"} }

        if os.getenv('AUGUR_ENV_ONLY', '0') != '1' and no_config_file == 0:
            try:
                __config_file = open(__config_file_path, 'r+')
            except:
                # logger.info('Couldn\'t open {}, attempting to create. If you have a augur.cfg, you can convert it to a json file using "make to-json"'.format(config_file))
                if not os.path.exists(__config_location):
                    os.makedirs(__config_location)
                __config_file = open(__config_file_path, 'w+')
                __config_bad = True


            # Options to export the loaded configuration as environment variables for Docker
           
            if __export_env:
                
                export_filename = os.getenv('AUGUR_ENV_EXPORT_FILE', 'augur.cfg.sh')
                __export_file = open(export_filename, 'w+')
                # logger.info('Exporting {} to environment variable export statements in {}'.format(config_file, export_filename))
                __export_file.write('#!/bin/bash\n')

            # Load the config file and return [section][name]
            try:
                config_text = __config_file.read()
                __config = json.loads(config_text)
                if name is not None:
                    try:
                        return(__config[section][name])
                    except:
                        return default
                else:
                    return(__config[section])

            except json.decoder.JSONDecodeError as e:
                if not __config_bad:
                    __using_config_file = False
                    # logger.error('%s could not be parsed, using defaults. Fix that file, or delete it and run this again to regenerate it. Error: %s', __config_file_path, str(e))

                __config = __default_config
                return(__config[section][name])



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
        if people and not multi_threaded_connection:
            self.cursor_people = cursor
            self.db_people = db
        elif not multi_threaded_connection:
            #self.cursor = cursor
            #self.db = db
            self.cursor_people = cursor
            self.db_people = db

        # else:

        #   db = MySQLdb.connect(
        #       host = db_host,
        #       user = db_user,
        #       passwd = db_pass,
        #       db = db_name,
        #       charset = 'utf8mb4',
        #       connect_timeout = 31536000)

        #   self.cursor = db.self.cursor(MySQLdb.self.cursors.DictCursor)
        
        # Figure out how much we're going to log
        self.log_level = self.get_setting('log_level')

        return db, cursor
        

    def get_setting(self, setting):

    # Get a setting from the database

        query = ("""SELECT value FROM settings WHERE setting=%s ORDER BY 
            last_modified DESC LIMIT 1""")
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
        logging.info("* %s\n" % status)
        if self.log_level == 'Debug' and level == 'Debug':
            return

        #if log_options.index(level) <= log_options.index(self.log_level):
        query = ("INSERT INTO utility_log (level,status) VALUES (%s,%s)")
        try:
            self.cursor.execute(query, (level, status))
            self.db.commit()
        except:
            # Set up the database
            json = self.read_config("Database", use_main_config=1)#self.cfg.migrate_database_config("Credentials")
            db_user = json['user']
            db_pass = json['password']
            db_name = json['database']
            db_host = json['host']
            db_port = json['port']
            db_user_people = json['user']
            db_pass_people = json['password']
            db_name_people = json['database']
            db_host_people = json['host']
            db_port_people = json['port']
            # Open a general-purpose connection
            db,cursor = self.database_connection(
                db_host,
                db_user,
                db_pass,
                db_name,
                db_port, False, False)
            self.cursor.execute(query, (level, status))
            self.db.commit()
