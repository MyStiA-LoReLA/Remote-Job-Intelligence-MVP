"""
ranker.py — 职位评分与排序模块

核心模块。根据技能标签和薪资计算每个职位的匹配分数，
然后按分数从高到低排序，输出推荐列表。
"""


def score_job(job):
    """
    计算单个职位的评分

    评分规则:
        - 包含 "python" 标签  +3 分
        - 包含 "devops" 标签  +3 分
        - 包含 "docker" 标签  +2 分
        - 薪水 > 3000         +2 分

    参数:
        job: 单个职位字典

    返回:
        整数分数
    """
    score = 0
    tags = [tag.lower() for tag in job.get("tags", [])]
    salary = job.get("salary", 0)

    if "python" in tags:
        score += 3

    if "devops" in tags:
        score += 3

    if "docker" in tags:
        score += 2

    if salary > 3000:
        score += 2

    return score


def rank_jobs(jobs):
    """
    给所有职位打分，并按分数从高到低排序

    参数:
        jobs: 职位列表

    返回:
        排序后的列表，每项包含原始信息 + score 字段
    """
    scored = []

    for job in jobs:
        job_with_score = dict(job)  # 复制一份，不修改原始数据
        job_with_score["score"] = score_job(job)
        scored.append(job_with_score)

    # 按分数从高到低排序
    ranked = sorted(scored, key=lambda j: j["score"], reverse=True)

    return ranked
