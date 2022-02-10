from github import Github
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', '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')
g = Github(token)
repo = g.get_repo("nozzy23/github_python_api")
issues = repo.get_issues(state="open")
pprint(issues.get_page(0))