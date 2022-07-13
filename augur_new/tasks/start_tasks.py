from .issue_tasks import *

pr_numbers = [70, 106, 170, 190, 192, 208, 213, 215, 216, 218, 223, 224, 226, 230, 237, 238, 240, 241, 248, 249, 250, 252, 253, 254, 255, 256, 257, 261, 268, 270, 273, 277, 281, 283, 288, 291, 303, 306, 309, 310, 311, 323, 324, 325, 334, 335, 338, 343, 346, 348, 350, 353, 355, 356, 357, 359, 360, 365, 369, 375, 381, 382, 388, 405, 408, 409, 410, 414, 418, 419, 420, 421, 422, 424, 425, 431, 433, 438, 445, 450, 454, 455, 456, 457, 460, 463, 468, 469, 470, 474, 475, 476, 477, 478, 479, 480, 481, 482, 484, 485, 486, 487, 488, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 504, 506, 507, 508, 509, 510, 512, 514]


@celery.task
def start_task(owner: str, repo):
    
    logger = logging.getLogger(start_task.__name__)
    session = TaskSession(logger)

    logger.info(f"Collecting data for {owner}/{repo}")
 
    start_task_list = []
    start_task_list.append(collect_pull_requests.s(owner, repo))
    # start_task_list.append(collect_issues.s(owner, repo))

    start_tasks_group = group(start_task_list)
    

    secondary_task_list = []
    # secondary_task_list.append(pull_request_reviews.s(owner, repo, pr_numbers))
    # secondary_task_list.append(collect_events.s(owner, repo))
    # secondary_task_list.append(collect_issue_and_pr_comments.s(owner, repo))
    
    secondary_task_group = group(secondary_task_list)

    third_task_list = []
    # third_task_list.append(process_contributors.s())
    
    third_task_group = group(third_task_list)


    job = chain(
        start_tasks_group,
        secondary_task_group,
        process_contributors.s(),
    )

    job.apply_async()