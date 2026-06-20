# Remote Job Intelligence MVP

A simple, beginner-friendly remote job recommendation system (Python CLI tool).

---

## Project Structure

`
job-intelligence/
├── data/
│   └── mock_jobs.py      # Mock RemoteOK API data
├── core/
│   ├── filter.py          # Job filtering module
│   ├── normalizer.py      # Data normalization module
│   └── ranker.py          # Scoring & ranking module (core)
├── cli/
│   └── main.py            # Entry point, runs the full pipeline
└── README.md
`

## Module Overview

| Layer | File | Purpose |
|-------|------|---------|
| Data | data/mock_jobs.py | Provides 20 mock job entries |
| Filter | core/filter.py | ilter_remote_jobs() - keeps only remote jobs |
| Normalizer | core/normalizer.py | 
ormalize_jobs() - unifies field format |
| Ranker | core/ranker.py | score_job() + 
ank_jobs() - scores and sorts |
| Entry | cli/main.py | Chains the pipeline and prints top 10 picks |

## Scoring Rules

| Condition | Points |
|-----------|--------|
| Tag contains "python" | +3 |
| Tag contains "devops" | +3 |
| Tag contains "docker" | +2 |
| Salary > 3000 | +2 |

## How to Run

### 1. Make sure you have Python 3 installed

`
python --version
`

### 2. Run the program

`
cd "Remote Job Intelligence MVP"
python cli/main.py
`

## What You Can Learn

If you're learning Python, this project helps you understand:

- How functions form a processing pipeline
- Using dictionaries to represent structured data
- List filtering and sorting
- Modular code organization
- CLI program entry structure

## Ideas for Extension

- Add tag-based filtering to ilter.py
- Define new scoring rules in 
anker.py
- Replace mock data with a local JSON file
- Build a simple Flask/Streamlit web UI in cli/app.py

---
*Built with Python 3 - no external dependencies required.*
