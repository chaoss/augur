from celery.utils.log import get_task_logger
from .celery import facadeApp


#!/usr/bin/env python3

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
import traceback
import sys, platform, imp, time, datetime, html.parser, subprocess, os, getopt, xlsxwriter, configparser, logging
from multiprocessing import Process, Queue
from facade_worker.facade01config import Config#increment_db, update_db, migrate_database_config, database_connection, get_setting, update_status, log_activity          
from facade_worker.facade02utilitymethods import update_repo_log, trim_commit, store_working_author, trim_author   
from facade_worker.facade03analyzecommit import analyze_commit
from facade_worker.facade04postanalysiscleanup import git_repo_cleanup
from facade_worker.facade05repofetch import git_repo_initialize, check_for_repo_updates, force_repo_updates, force_repo_analysis, git_repo_updates
from facade_worker.facade06analyze import analysis
from facade_worker.facade07rebuildcache import nuke_affiliations, fill_empty_affiliations, invalidate_caches, rebuild_unknown_affiliation_and_web_caches

#from contributor_interfaceable.facade08contributorinterfaceable import ContributorInterfaceable

from contributor_interfaceable.contributor_interface import ContributorInterfaceable as ContribInterface 

from workers.util import read_config
from workers.worker_base import Worker


html = html.parser.HTMLParser()

logger = get_task_logger(__name__)

#TODO: talk about weird command line arguments.

#OPTIONS are completely disregarded from facade instead provided by config.
@facadeApp.task
def commits_model(config,message):
    # Figure out what we need to do
    limited_run = config["limited_run"]
    delete_marked_repos = config["delete_marked_repos"]
    pull_repos = config["pull_repos"]
    clone_repos = config["clone_repos"]
    check_updates = config["check_updates"]
    force_updates = config["force_updates"]
    run_analysis = config["run_analysis"]
    force_analysis = config["force_analysis"]
    nuke_stored_affiliations = config["nuke_stored_affiliations"]
    fix_affiliations = config["fix_affiliations"]
    force_invalidate_caches = config["force_invalidate_caches"]
    rebuild_caches = config["rebuild_caches"] #if abs((datetime.datetime.strptime(self.cfg.get_setting('aliases_processed')[:-3], 
        # '%Y-%m-%d %I:%M:%S.%f') - datetime.datetime.now()).total_seconds()) // 3600 > int(self.cfg.get_setting(
        #   'update_frequency')) else 0
    force_invalidate_caches = config["force_invalidate_caches"]
    create_xlsx_summary_files = config["create_xlsx_summary_files"]
    multithreaded = config["multithreaded"]

    # Get the location of the directory where git repos are stored
    repo_base_directory = config['repo_base_directory']

    #Determine if it's safe to start the script
    current_status = config['utility_status']

    if current_status != 'Idle':
        logger.error('Something is already running, aborting maintenance and analysis.\nIt is unsafe to continue.')
        # sys.exit(1)
    if len(repo_base_directory) == 0:
        logger.error('No base directory. It is unsafe to continue.')
        logger.error('Failed: No base directory')
        sys.exit(1)

    # Begin working

    start_time = time.time()
    logger.info('Running facade-worker')

    cfg = Config(logger)

    if not limited_run or (limited_run and delete_marked_repos):
        git_repo_cleanup(cfg)

    if not limited_run or (limited_run and clone_repos):
        git_repo_initialize(cfg)

    if not limited_run or (limited_run and check_updates):
        check_for_repo_updates(cfg)

    if force_updates:
        force_repo_updates(cfg)

    if not limited_run or (limited_run and pull_repos):
        git_repo_updates(cfg)

    if force_analysis:
        force_repo_analysis(cfg)

    #TODO: rewrite the contributer interface.
    #Doesn't really need to be a class at all.
    github_interface = ContribInterface(config=config, logger=logger) 
    #Give analysis the github interface so that it can make API calls
    if not limited_run or (limited_run and run_analysis):
        analysis(cfg, multithreaded, interface=github_interface)
    

    ### moved up by spg on 12/1/2021
    #Interface with the contributor worker and inserts relevant data by repo
    cfg.update_status('Updating Contributors')
    cfg.log_activity('Info', 'Updating Contributors with commits')
    query = ("SELECT repo_id FROM repo")

    cfg.cursor.execute(query)

    all_repos = list(cfg.cursor)

    for repo in all_repos:
        logger.info(f"Processing repo {repo}")
        github_interface.insert_facade_contributors(repo[0],multithreaded=multithreaded)
        logger.info(f"Processing repo contributors for repo: {repo}")
    

    if nuke_stored_affiliations:
        nuke_affiliations(cfg)

    if not limited_run or (limited_run and fix_affiliations):
        fill_empty_affiliations(cfg)
    

    if force_invalidate_caches:
        invalidate_caches(cfg)

    if not limited_run or (limited_run and rebuild_caches):
        rebuild_unknown_affiliation_and_web_caches(cfg)

    if not limited_run or (limited_run and create_xlsx_summary_files):

        cfg.log_activity('Info','Creating summary Excel files')

        # from excel_generators import *

        cfg.log_activity('Info','Creating summary Excel files (complete)')
    
    # All done
    cfg.update_status('Idle')
    cfg.log_activity('Quiet','facade-worker.py completed')

    elapsed_time = time.time() - start_time

    print('\nCompleted in %s\n' % datetime.timedelta(seconds=int(elapsed_time)))

    cfg.cursor.close()
    cfg.cursor_people.close()
    cfg.db.close()
    cfg.db_people.close()

    

