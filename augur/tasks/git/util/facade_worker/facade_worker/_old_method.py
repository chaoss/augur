"""
def get_repo_commit_count(logger, facade_helper, repo_git):

	repo = get_repo_by_repo_git(repo_git)
    
	absolute_path = get_absolute_repo_path(facade_helper.repo_base_directory, repo.repo_id, repo.repo_path,repo.repo_name)
	repo_loc = (f"{absolute_path}/.git")

	logger.debug(f"loc: {repo_loc}")
	logger.debug(f"path: {repo.repo_path}")

	# Check if the .git directory exists
	if not os.path.exists(repo_loc):
		try:
			logger.error(f"Ran into an error with {repo_loc}. Checking another strategy without .git extension.")
			repo_loc = absolute_path 
			if not os.path.exists(repo_loc):
				raise FileNotFoundError(f"The directory {repo_loc} does not exist.")
		except Exception as e: 
			raise FileNotFoundError(f"The directory {absolute_path} does not exist, also {repo_loc} does not exist.")
	
	# if there are no branches then the repo is empty
	if count_branches(repo_loc) == 0:
		return 0

	try:
		check_commit_count_cmd = check_output(
			["git", "--git-dir", repo_loc, "rev-list", "--count", "HEAD"],
			stderr=subprocess.PIPE)
	except CalledProcessError as e:
		logger.error(f"Ran into {e}: {e.output} {e.stderr} \n With return code {e.returncode}")
		raise e
		

	commit_count = int(check_commit_count_cmd)

	return commit_count
"""