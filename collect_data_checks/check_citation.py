import re
import requests
from bs4 import BeautifulSoup
from .githubInfo import *
from rich import print
from rich.console import Console





def check_for_citation( path: str, name: str) -> bool:
    console = Console()
    console.print('Checking citation file...', style = 'yellow')
    git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(path)
    try:
            r = requests.get(git_repo_link)
            html_doc = r.text
            soup = BeautifulSoup(html_doc,'html5lib')
            file = soup.find_all(title=re.compile(name))
            if file:
                return True
            else:
                return False
    except Exception:
            return False

# print(check_for_citation( repo_path, 'CITATION.CFF'))