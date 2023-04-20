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
# SPDX-License-Identifier:	Apache-2.0

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
from subprocess import check_output
import os
import getopt
import xlsxwriter
import configparser
import sqlalchemy as s
from .config import get_database_args_from_env
from augur.application.db.models.augur_data import *
from .config import FacadeSession as FacadeSession
from augur.tasks.util.worker_util import calculate_date_weight_from_timestamps
#from augur.tasks.git.util.facade_worker.facade

def update_repo_log(session, repos_id,status):

# Log a repo's fetch status
	session.log_activity("Info",f"{status} {repos_id}")
	#log_message = ("INSERT INTO repos_fetch_log (repos_id,status) "
	#	"VALUES (%s,%s)")
	try:
		log_message = s.sql.text("""INSERT INTO repos_fetch_log (repos_id,status) 
            VALUES (:repo_id,:repo_status)""").bindparams(repo_id=repos_id,repo_status=status)

		#session.insert_data(data,t_repos_fetch_log,['repos_id','status'])
		session.execute_sql(log_message)
	except Exception as e:
		session.logger.error(f"Ran into error in update_repo_log: {e}")
		pass

def trim_commit(session, repo_id,commit):

# Quickly remove a given commit

	remove_commit = s.sql.text("""DELETE FROM commits
		WHERE repo_id=:repo_id
		AND cmt_commit_hash=:hash""").bindparams(repo_id=repo_id,hash=commit)

	 
	 
	session.execute_sql(remove_commit)

	session.log_activity('Debug',f"Trimmed commit: {commit}")

def store_working_author(session, email):

# Store the working author during affiliation discovery, in case it is
# interrupted and needs to be trimmed.

	store = s.sql.text("""UPDATE settings
		SET value = :email
		WHERE setting = 'working_author'
		""").bindparams(email=email)

	session.execute_sql(store)

	session.log_activity('Debug',f"Stored working author: {email}")

def trim_author(session, email):

# Remove the affiliations associated with an email. Used when an analysis is
# interrupted during affiliation layering, and the data will be corrupt.

	trim = s.sql.text("""UPDATE commits 
		SET cmt_author_affiliation = NULL 
		WHERE cmt_author_email = :email
		""").bindparams(email=email)

	 
	 
	session.execute_sql(trim)

	trim = s.sql.text("""UPDATE commits
		SET cmt_committer_affiliation = NULL
		WHERE cmt_committer_email = :email
		""").bindparams(email=email)

	session.execute_sql(trim)

	store_working_author(session, 'done')

	session.log_activity('Debug',f"Trimmed working author: {email}")

def get_absolute_repo_path(repo_base_dir, repo_group_id, repo_path, repo_name):
	
	return f"{repo_base_dir}{repo_group_id}/{repo_path}{repo_name}"

def get_parent_commits_set(absolute_repo_path, start_date):
	
	parents = subprocess.Popen(["git --git-dir %s log --ignore-missing "
								"--pretty=format:'%%H' --since=%s" % (absolute_repo_path,start_date)],
	stdout=subprocess.PIPE, shell=True)

	parent_commits = set(parents.stdout.read().decode("utf-8",errors="ignore").split(os.linesep))

	# If there are no commits in the range, we still get a blank entry in
	# the set. Remove it, as it messes with the calculations

	if '' in parent_commits:
		parent_commits.remove('')

	return parent_commits


def get_existing_commits_set(session, repo_id):

	find_existing = s.sql.text("""SELECT DISTINCT cmt_commit_hash FROM commits WHERE repo_id=:repo_id
		""").bindparams(repo_id=repo_id)

	existing_commits = [commit['cmt_commit_hash'] for commit in session.fetchall_data_from_sql_text(find_existing)]

	return set(existing_commits)


def get_repo_commit_count(session,repo_git):
	
	repo = Repo.get_by_repo_git(session, repo_git)
	

	absolute_path = get_absolute_repo_path(session.repo_base_directory, repo.repo_group_id, repo.repo_path, repo.repo_name)
	repo_loc = (f"{absolute_path}/.git")

	#git --git-dir <.git directory> rev-list --count HEAD
	check_commit_count_cmd = check_output(["git","--git-dir",repo_loc, "rev-list", "--count", "HEAD"])

	commit_count = int(check_commit_count_cmd)

	return commit_count

def get_facade_weight_time_factor(session,repo_git):
	repo = Repo.get_by_repo_git(session, repo_git)
	
	try:
		status = repo.collection_status[0]
		time_factor = calculate_date_weight_from_timestamps(repo.repo_added, status.facade_data_last_collected)
	except IndexError:
		time_factor = calculate_date_weight_from_timestamps(repo.repo_added, None)
	
	#Adjust for commits.
	time_factor *= 1.2

	return  time_factor


def get_repo_weight_by_commit(logger,repo_git):
	with FacadeSession(logger) as session:
		return get_repo_commit_count(session, repo_git) - get_facade_weight_time_factor(session, repo_git)
