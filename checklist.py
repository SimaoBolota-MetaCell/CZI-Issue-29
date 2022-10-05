
from githubInfo import *

repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'


git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(repo_path)
# get the current GitHub Repository README.md link, in which the search for citation will happen
README_LINK = git_repo_link + '/blob/%s/README.md'%(git_base_branch)

print(README_LINK)


import json, requests


while True:
    all_contributors = list()
    page_count = 1
    contributors = requests.get("https://api.github.com/repos/SimaoBolota-MetaCell/CZI-Citation-Final-draft/contributors?page=%d"%page_count)
    if contributors != None and contributors.status_code == 200 and len(contributors.json()) > 0:
        all_contributors = all_contributors + contributors.json()
    else:
        break
    page_count = page_count + 1

for single_contributors in all_contributors:
    contributor_usernames = list()
    single_contributors_list = list(single_contributors['login'].split(" "))
    contributor_usernames = contributor_usernames + single_contributors_list


    print("-------------------%d" %contributor_usernames)

from bs4 import BeautifulSoup

for contributor_username in contributor_usernames:
    print(contributor_username)
# github_html = requests.get(f'https://github.com/{username}').text
# soup = BeautifulSoup(github_html, "html.parser")


# something2 = list()
# while True:
#     sometyhing = requests.get("https://api.github.com/users/SimaoBolota-MetaCell")
#     if sometyhing != None and sometyhing.status_code == 200 and len(sometyhing.json()) > 0:
#        print(sometyhing)
#        print(sometyhing.json())



# display_name

# summary_sentence

# intro_paragraph

# intro_video

# intro_screenshot

# usage_overview

# source_code_link

# support_channel_link

# submit_issues_link

# author_names