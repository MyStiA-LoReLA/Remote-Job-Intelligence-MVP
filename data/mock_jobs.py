"""
mock_jobs.py — 模拟 RemoteOK API 返回的职位数据

这个模块负责提供测试用的 mock 职位数据。
每个 job 是一个字典，包含 title, company, remote, tags, salary 字段。
"""


def get_mock_jobs():
    """返回一组模拟的职位数据"""
    jobs = [
        {
            "title": "Senior Python Developer",
            "company": "TechCorp",
            "remote": True,
            "tags": ["python", "django", "postgresql"],
            "salary": 5000,
        },
        {
            "title": "DevOps Engineer",
            "company": "CloudBase",
            "remote": True,
            "tags": ["devops", "docker", "kubernetes", "aws"],
            "salary": 4500,
        },
        {
            "title": "Frontend Developer",
            "company": "WebStudio",
            "remote": True,
            "tags": ["javascript", "react", "css"],
            "salary": 3500,
        },
        {
            "title": "Full Stack Developer",
            "company": "StartupXYZ",
            "remote": False,
            "tags": ["python", "javascript", "react", "node"],
            "salary": 4000,
        },
        {
            "title": "Data Scientist",
            "company": "DataFlow",
            "remote": True,
            "tags": ["python", "machine-learning", "tensorflow"],
            "salary": 6000,
        },
        {
            "title": "Site Reliability Engineer",
            "company": "ReliableOps",
            "remote": True,
            "tags": ["devops", "docker", "kubernetes", "linux"],
            "salary": 5500,
        },
        {
            "title": "Junior Python Developer",
            "company": "CodeLab",
            "remote": True,
            "tags": ["python", "flask", "sql"],
            "salary": 2500,
        },
        {
            "title": "Marketing Manager",
            "company": "BrandCo",
            "remote": True,
            "tags": ["marketing", "seo", "content"],
            "salary": 3000,
        },
        {
            "title": "Docker Specialist",
            "company": "ContainerZone",
            "remote": True,
            "tags": ["docker", "linux", "ci-cd"],
            "salary": 4200,
        },
        {
            "title": "QA Engineer",
            "company": "TestLab",
            "remote": False,
            "tags": ["testing", "selenium", "python"],
            "salary": 2800,
        },
        {
            "title": "Product Manager",
            "company": "ProductHub",
            "remote": True,
            "tags": ["product", "agile", "analytics"],
            "salary": 4800,
        },
        {
            "title": "DevOps Intern",
            "company": "CloudBase",
            "remote": False,
            "tags": ["devops", "docker", "linux"],
            "salary": 1500,
        },
        {
            "title": "Python Backend Lead",
            "company": "ScaleUp",
            "remote": True,
            "tags": ["python", "docker", "postgresql", "redis"],
            "salary": 7000,
        },
        {
            "title": "UX Designer",
            "company": "DesignStudio",
            "remote": True,
            "tags": ["ux", "figma", "research"],
            "salary": 3800,
        },
        {
            "title": "Security Engineer",
            "company": "SecureNet",
            "remote": True,
            "tags": ["security", "devops", "python"],
            "salary": 5200,
        },
        {
            "title": "Graphic Designer",
            "company": "CreativeX",
            "remote": False,
            "tags": ["photoshop", "illustrator", "design"],
            "salary": 2600,
        },
        {
            "title": "Cloud Architect",
            "company": "CloudBase",
            "remote": True,
            "tags": ["aws", "devops", "docker", "terraform"],
            "salary": 6500,
        },
        {
            "title": "Technical Writer",
            "company": "DocuMatic",
            "remote": True,
            "tags": ["documentation", "markdown", "api"],
            "salary": 3200,
        },
        {
            "title": "Junior DevOps Engineer",
            "company": "StackOps",
            "remote": True,
            "tags": ["devops", "docker", "ci-cd"],
            "salary": 3000,
        },
        {
            "title": "Data Analyst",
            "company": "InsightCo",
            "remote": False,
            "tags": ["python", "sql", "excel"],
            "salary": 3200,
        },
    ]

    return jobs
