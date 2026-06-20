# Remote Job Intelligence MVP

一个简单的、适合初学者的远程职位智能推荐系统（Python 命令行工具）。

---

## 项目结构

```
job-intelligence/
├── data/
│   └── mock_jobs.py      # 模拟 RemoteOK API 数据
├── core/
│   ├── filter.py          # 职位过滤模块
│   ├── normalizer.py      # 数据标准化模块
│   └── ranker.py          # 评分 & 排序模块（核心）
├── cli/
│   └── main.py            # 程序入口，运行整个流程
└── README.md
```

## 各模块作用

| 模块 | 文件 | 功能 |
|------|------|------|
| 数据层 | `data/mock_jobs.py` | 提供 20 条模拟职位数据 |
| 过滤 | `core/filter.py` | `filter_remote_jobs()` — 只保留远程职位 |
| 标准化 | `core/normalizer.py` | `normalize_jobs()` — 统一字段格式 |
| 排序 | `core/ranker.py` | `score_job()` + `rank_jobs()` — 评分并排序 |
| 入口 | `cli/main.py` | 串联完整流程并输出前 10 个推荐 |

## 评分规则

| 条件 | 加分 |
|------|------|
| 技能包含 "python" | +3 |
| 技能包含 "devops" | +3 |
| 技能包含 "docker" | +2 |
| 薪资 > 3000 | +2 |

## 如何运行

### 1. 确保安装了 Python 3

```
python --version
```

### 2. 运行程序

```
cd job-intelligence
python cli/main.py
```

## 学习要点

如果你在学 Python，这个项目可以帮助你理解：

- 函数如何组合成一条处理流水线
- 用字典表示结构化数据
- 列表过滤与排序
- 模块化组织代码
- 命令行程序的入口结构

## 扩展思路（学有余力可以自己尝试）

- 给 `filter.py` 增加按技能标签过滤的功能
- 给 `ranker.py` 增加新的评分规则
- 把 mock 数据改成从本地 JSON 文件读取
- 在 `cli/` 里加一个 `app.py` 用 Flask/Streamlit 做一个简单网页

---
*Built with Python 3 - no external dependencies required.*
