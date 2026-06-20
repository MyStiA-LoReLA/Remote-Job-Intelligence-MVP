"""
normalizer.py — 数据标准化模块

确保每个 job 字典都包含统一的字段结构，
防止下游模块因为缺少字段而出错。
"""


def normalize_jobs(jobs):
    """
    统一职位数据格式，补全缺失字段

    参数:
        jobs: 原始职位列表

    返回:
        标准化后的职位列表
    """
    normalized = []

    for job in jobs:
        normalized_job = {
            "title": job.get("title", "Unknown Title"),
            "company": job.get("company", "Unknown Company"),
            "remote": job.get("remote", False),
            "tags": job.get("tags", []),
            "salary": job.get("salary", 0),
        }
        normalized.append(normalized_job)

    return normalized
