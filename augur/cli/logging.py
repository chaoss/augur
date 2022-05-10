#SPDX-License-Identifier: MIT
import click
import os
from os import walk
import time
from datetime import datetime
from augur.cli import pass_logs_dir

@click.group("logging", short_help="View Augur's log files")
def cli():
    pass

@cli.command("directory")
@pass_logs_dir
def directory(logs_dir):
    """
    Print the location of Augur's logs directory
    """
    print(logs_dir)


@cli.command("log_query")
@click.argument("tags")
@click.argument("worker")
@click.option("--limit", 'limit', default=10)
@click.option("--output", 'output', default=None)
@pass_logs_dir
def log_query(logs_dir, tags, worker, limit, output):
    """
    Query augur logs with tags comma separated
    """
    start_time = time.time()
    if not os.path.exists(logs_dir + "/workers"):
        print("Worker logs have not been generated yet.")
        return

    if tags == '':
        print("Tags are required!")
        return
        
    tagset = set(tags.split(','))

    if worker == '':
        print("Worker is required!")
        return

    if not os.path.exists(f"{logs_dir}/workers/{worker}"):
        print("Logs for this worker do not exist. (Check spelling?)")
        return
        
    file_list = os.listdir(f"{logs_dir}/workers/{worker}")
    log_file = ""
    for file in file_list:
        if file.endswith("collection.log"):
            log_file = file
            break
    log_file_path = f"{logs_dir}/workers/{worker}/{log_file}"

    worker_file = open(log_file_path)
    worker_file_lines = worker_file.readlines()
    worker_file_lines = [value for value in worker_file_lines if value != '\n']
    worker_file.close()
    output_logs = []
    current_output_log = ""
    log_limit = limit
    line_index = len(worker_file_lines) - 1
    saved_line_index = 0
    # for each line, back to front
    while line_index >= 0:
        if '|' in worker_file_lines[line_index]:
            linesep = worker_file_lines[line_index].split('|')
            linetags = linesep[1].split(' ')
            if not tagset <= set(linetags):
                line_index -= 1
                continue
            saved_line_index = line_index
            current_output_log = worker_file_lines[line_index]
            while line_index + 1 != len(worker_file_lines) and '|' not in worker_file_lines[line_index + 1]:
                line_index += 1
                current_output_log += worker_file_lines[line_index]
            output_logs.insert(0, current_output_log)
            line_index = saved_line_index - 1
            log_limit -= 1
            if log_limit == 0:
                break
        else:
            line_index -= 1
            continue
    run_time = round(1000 * (time.time() - start_time), 0)
    log_count = len(output_logs)
    if log_count == 0:
        print("Query returned no results.")
    else:
        print("--- QUERY RETURNED " + str(log_count) + " RESULTS (in %sms) ---\n" % run_time)
        for value in output_logs:
            print(value)
        print("--- END OF RESULTS ---")
        if output != None:
            try:
                output_file = open(output, "w")
                output_file.write("Query ran at " + str(datetime.now()) + ". Query parameters: tags=" + tags + ", worker=" + worker + '\n')
                output_file.write("--- QUERY RETURNED " + str(log_count) + " RESULTS (in %sms) ---\n" % run_time)
                for value in output_logs:
                    output_file.write(value + '\n')
                output_file.write("--- END OF RESULTS ---")
                output_file.close()
            except Exception as e:
                print("Output file entered is not valid or no permission to write to this file.")


@cli.command("errors")
@click.argument("worker", default="all")
@pass_logs_dir
def errors(logs_dir, worker):
    """
    Output error messages of the main Augur and all worker logfiles or a specific worker logfile
    """
    root_log_dir = logs_dir
    worker_log_dir = logs_dir + "/workers/"
    if worker is None:
        worker = "all"

    if worker == "all":
        files = []
        directories = []
        for (_, _, filenames) in walk(root_log_dir):
            for file in filenames:
                if file.endswith(".err"):
                    print_log(file, root_log_dir)
            break

        files = []
        directories = []
        for (dirpath, dirnames, filenames) in walk(worker_log_dir):
            directories.extend(dirnames)
            break

        for directory in directories:
            specific_worker_log_dir = worker_log_dir + directory
            for (_, _, filenames) in walk(specific_worker_log_dir):
                files.extend(filenames)
                for file in [file for file in filenames if "collection" in file and file.endswith(".err")]:
                    print_log(file, specific_worker_log_dir)
                break
    else:
        files = []
        specific_worker_log_dir = worker_log_dir + "/" + worker + "/"
        for (_, _, filenames) in walk(specific_worker_log_dir):
            files.extend(filenames)
            for file in [file for file in filenames if "collection" in file and file.endswith(".err")]:
                print_log(file, specific_worker_log_dir)
            break

def print_log(file, log_dir):
    f = open(log_dir + "/" + file)
    result = f.readlines()
    print("********** Logfile: " + file)
    for log in result:
        print(log.strip())
    print()

@cli.command("tail")
@click.argument("lines", default=20)
@pass_logs_dir
def tail(logs_dir, lines):
    """
    Output the last n lines of the main Augur and worker logfiles
    """
    root_log_dir = logs_dir
    worker_log_dir = logs_dir + "/workers/"
    if lines is None:
        lines = 20

    files = []
    directories = []
    for (_, _, filenames) in walk(root_log_dir):
        for file in filenames:
            result = _tail(open(root_log_dir + "/" + file), lines)
            print("********** Logfile: " + file)
            for log in result:
                print(log.strip())
            print()
        break

    files = []
    directories = []
    for (dirpath, dirnames, filenames) in walk(worker_log_dir):
        directories.extend(dirnames)
        break

    for directory in directories:
        specific_worker_log_dir = worker_log_dir + directory
        for (_, _, filenames) in walk(specific_worker_log_dir):
            files.extend(filenames)

            for file in [file for file in filenames if "collection" in file]:
                result = _tail(open(specific_worker_log_dir + "/" + file), lines)
                print("********** Logfile: " + file)
                for log in result:
                    print(log.strip())
                print()
            break

def _tail(f, lines=20, _buffer=4098):
    lines_found = []

    # block counter will be multiplied by buffer
    # to get the block size from the end
    block_counter = -1

    # loop until we find X lines
    while len(lines_found) < lines:
        try:
            f.seek(block_counter * _buffer, os.SEEK_END)
        except IOError:  # either file is too small, or too many lines requested
            f.seek(0)
            lines_found = f.readlines()
            break

        lines_found = f.readlines()

        # we found enough lines, get out
        # Removed this line because it was redundant the while will catch
        # it, I left it for history
        # if len(lines_found) > lines:
        #    break

        # decrement the block counter to get the
        # next X bytes
        block_counter -= 1

    return lines_found[-lines:]