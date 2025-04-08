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
import subprocess
from subprocess import check_output, CalledProcessError
import os
import sqlalchemy as s
from augur.application.db.models import *
from .config import FacadeHelper as FacadeHelper
from augur.tasks.util.worker_util import calculate_date_weight_from_timestamps
from augur.application.db.lib import execute_sql, fetchall_data_from_sql_text, remove_working_commits_by_repo_id_and_hashes, remove_commits_by_repo_id_and_hashes, get_repo_by_repo_git, get_session
from augur.application.db.util import execute_session_query
#from augur.tasks.git.util.facade_worker.facade

def update_repo_log(logger, facade_helper, repos_id,status):

# Log a repo's fetch status
	facade_helper.log_activity("Info",f"{status} {repos_id}")
	#log_message = ("INSERT INTO repos_fetch_log (repos_id,status) "
	#	"VALUES (%s,%s)")
	try:
		log_message = s.sql.text("""INSERT INTO repos_fetch_log (repos_id,status) 
            VALUES (:repo_id,:repo_status)""").bindparams(repo_id=repos_id,repo_status=status)

		#bulk_insert_dicts(data,t_repos_fetch_log,['repos_id','status'])
		execute_sql(log_message)
	except Exception as e:
		logger.error(f"Ran into error in update_repo_log: {e}")
		pass

def trim_commits(facade_helper, repo_id,commits):

	# Quickly remove a given commit

	if len(commits):
		remove_commits_by_repo_id_and_hashes(repo_id, commits)
	
		# Remove the working commit.
		remove_working_commits_by_repo_id_and_hashes(repo_id, commits)

	for commit in commits:
		facade_helper.log_activity('Debug',f"Trimmed commit: {commit}")
		facade_helper.log_activity('Debug',f"Removed working commit: {commit}")

def store_working_author(facade_helper, email):

# Store the working author during affiliation discovery, in case it is
# interrupted and needs to be trimmed.

	store = s.sql.text("""UPDATE settings
		SET value = :email
		WHERE setting = 'working_author'
		""").bindparams(email=email)

	execute_sql(store)

	facade_helper.log_activity('Debug',f"Stored working author: {email}")

def trim_author(facade_helper, email):

# Remove the affiliations associated with an email. Used when an analysis is
# interrupted during affiliation layering, and the data will be corrupt.

	trim = s.sql.text("""UPDATE commits 
		SET cmt_author_affiliation = NULL 
		WHERE cmt_author_email = :email
		""").bindparams(email=email)
	execute_sql(trim)

	trim = s.sql.text("""UPDATE commits
		SET cmt_committer_affiliation = NULL
		WHERE cmt_committer_email = :email
		""").bindparams(email=email)
	execute_sql(trim)

	store_working_author(facade_helper, 'done')

	facade_helper.log_activity('Debug',f"Trimmed working author: {email}")

def get_absolute_repo_path(repo_base_dir, repo_id, repo_path,repo_name):
	
	return f"{repo_base_dir}{repo_id}-{repo_path}/{repo_name}"

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


def get_existing_commits_set(repo_id):

	find_existing = s.sql.text("""SELECT DISTINCT cmt_commit_hash FROM commits WHERE repo_id=:repo_id
		""").bindparams(repo_id=repo_id)

	existing_commits = [commit['cmt_commit_hash'] for commit in fetchall_data_from_sql_text(find_existing)]

	return set(existing_commits)


def count_branches(git_dir):
    branches_dir = os.path.join(git_dir, 'refs', 'heads')
    return sum(1 for _ in os.scandir(branches_dir))

def get_repo_commit_count(logger, facade_helper, repo_git):
    repo = get_repo_by_repo_git(repo_git)
    
    absolute_path = get_absolute_repo_path(
        facade_helper.repo_base_directory,
        repo.repo_id,
        repo.repo_path,
        repo.repo_name
    )
    repo_loc = f"{absolute_path}/.git"

    logger.debug(f"Repository location: {repo_loc}")
    logger.debug(f"Repository path: {repo.repo_path}")

    # Determine the correct repository directory.
    if not os.path.exists(repo_loc):
        logger.error(f"Directory not found: {repo_loc}. Trying without '.git' extension.")
        repo_loc = absolute_path 
        if not os.path.exists(repo_loc):
            raise FileNotFoundError(f"Neither {absolute_path} nor {repo_loc} exist.")

    # If the repository does not have any branches, it is considered empty.
    if count_branches(repo_loc) == 0:
        logger.info("Repository is empty; no branches found.")
        return 0

    def get_commit_count():
        """Attempt to get commit count using git rev-list."""
        output = check_output(
            ["git", "--git-dir", repo_loc, "rev-list", "--count", "HEAD"],
            stderr=subprocess.PIPE
        )
        return int(output.decode('utf-8').strip())

    # First attempt to count commits.
    try:
        commit_count = get_commit_count()
        return commit_count
    except CalledProcessError as e:
        stderr_msg = e.stderr.decode('utf-8') if e.stderr else ""
        logger.error(
            f"Error running 'git rev-list --count HEAD' in {repo_loc}: "
            f"Return code {e.returncode}. Stderr: {stderr_msg}"
        )
        # Check for error indications that might suggest corruption.
        if e.returncode == 128 and ("Could not read" in stderr_msg or "unknown revision" in stderr_msg.lower()):
            logger.info("Detected repository issues. Running 'git fsck' and 'git gc --prune=now' to attempt repair.")
            # Run git fsck.
            try:
                fsck_output = check_output(
                    ["git", "--git-dir", repo_loc, "fsck"],
                    stderr=subprocess.PIPE
                )
                logger.info("git fsck output: " + fsck_output.decode('utf-8').strip())
            except Exception as fsck_e:
                logger.error(f"Error running 'git fsck': {fsck_e}")
            # Run git gc with prune.
            try:
                gc_output = check_output(
                    ["git", "--git-dir", repo_loc, "gc", "--prune=now"],
                    stderr=subprocess.PIPE
                )
                logger.info("git gc --prune=now output: " + gc_output.decode('utf-8').strip())
            except Exception as gc_e:
                logger.error(f"Error running 'git gc --prune=now': {gc_e}")

            # Retry the commit count logic.
            try:
                commit_count = get_commit_count()
                return commit_count
            except CalledProcessError as re:
                logger.error(
                    f"Retry of 'git rev-list --count HEAD' failed in {repo_loc}: "
                    f"Return code {re.returncode}. Stderr: {re.stderr.decode('utf-8') if re.stderr else ''}"
                )
                return 0
        else:
            # If the error does not indicate the expected repository issues, re-raise.
            raise e

    except Exception as e:
        logger.error(f"Unexpected error while counting commits: {str(e)}")
        raise e

def get_facade_weight_time_factor(repo_git):

	with get_session() as session:

		query = session.query(Repo).filter(Repo.repo_git == repo_git)
		repo = execute_session_query(query, 'one')

		try:
			status = repo.collection_status[0]
			time_factor = calculate_date_weight_from_timestamps(repo.repo_added, status.facade_data_last_collected)
		except IndexError:
			time_factor = calculate_date_weight_from_timestamps(repo.repo_added, None)
		
		#Adjust for commits.
		time_factor *= 1.2

		return  time_factor

def get_facade_weight_with_commit_count(repo_git, commit_count):
	return commit_count - get_facade_weight_time_factor(repo_git)


def get_repo_weight_by_commit(logger, repo_git):
	facade_helper = FacadeHelper(logger)
	return get_repo_commit_count(logger, facade_helper, repo_git) - get_facade_weight_time_factor(repo_git)
	

def update_facade_scheduling_fields(repo_git, weight, commit_count):

	repo = get_repo_by_repo_git(repo_git)

	with get_session() as session:

		update_query = (
			s.update(CollectionStatus)
			.where(CollectionStatus.repo_id == repo.repo_id)
			.values(facade_weight=weight,commit_sum=commit_count)
		)

		session.execute(update_query)
		session.commit()



