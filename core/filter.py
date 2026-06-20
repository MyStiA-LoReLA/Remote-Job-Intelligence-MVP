"""
filter.py — 职位过滤模块

负责根据条件筛选职位，目前只做远程职位过滤。
未来可以扩展出根据标签、薪资等条件过滤的功能。
"""


def filter_remote_jobs(jobs):
    """
    只保留 remote = True 的职位

    参数:
        jobs: 职位列表，每个元素是一个字典

    返回:
        过滤后的新列表，只包含远程职位
    """
    remote_jobs = []

    for job in jobs:
        if job.get("remote") is True:
            remote_jobs.append(job)

    return remote_jobs
