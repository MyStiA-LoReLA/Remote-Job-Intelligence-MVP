"""
main.py -- 远程职位智能推荐系统的 CLI 入口

完整流程:
  1. 加载 mock 数据
  2. 过滤出远程职位
  3. 标准化数据
  4. 计算评分并排序
  5. 打印前 10 个推荐结果
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from data.mock_jobs import get_mock_jobs
from core.filter import filter_remote_jobs
from core.normalizer import normalize_jobs
from core.ranker import rank_jobs


def print_header():
    print("=" * 64)
    print("   Remote Job Intelligence MVP")
    print("   远程职位智能推荐系统")
    print("=" * 64)


def print_result(job, rank):
    """打印单个推荐结果"""
    print(f"\n  #{rank}")
    print(f"  {job['title']} @ {job['company']}")
    print(f"  Salary: ${job['salary']}  |  Score: {job['score']}")
    print(f"  Tags: {', '.join(job['tags'])}")
    print(f"  {'-' * 56}")


def main():
    print_header()

    print("\n[1/4] Loading mock job data...")
    all_jobs = get_mock_jobs()
    print(f"       Total jobs loaded: {len(all_jobs)}")

    print("\n[2/4] Filtering remote jobs...")
    remote_jobs = filter_remote_jobs(all_jobs)
    print(f"       Remote jobs: {len(remote_jobs)}")

    print("\n[3/4] Normalizing job data...")
    normalized = normalize_jobs(remote_jobs)

    print("\n[4/4] Scoring & ranking jobs...")
    ranked = rank_jobs(normalized)

    print("\n" + "=" * 64)
    print("   Top 10 Recommended Remote Jobs")
    print("=" * 64)

    top_n = ranked[:10]

    for i, job in enumerate(top_n, start=1):
        print_result(job, i)

    print("\nDone. Happy remote job hunting!")


if __name__ == "__main__":
    main()
