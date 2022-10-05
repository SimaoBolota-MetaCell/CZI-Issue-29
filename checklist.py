
from githubInfo import *

repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'


git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(repo_path)
# get the current GitHub Repository README.md link, in which the search for citation will happen
README_LINK = git_repo_link + '/blob/%s/README.md'%(git_base_branch)

print(README_LINK)


import json, requests
all_contributors = list()
page_count = 1
while True:
    contributors = requests.get("https://api.github.com/SimaoBolota-MetaCell/CZI-Issue-29/rubinius/contributors?page=%d"%page_count)
    if contributors != None and contributors.status_code == 200 and len(contributors.json()) > 0:
        all_contributors = all_contributors + contributors.json()
    else:
        break
    page_count = page_count + 1
count=len(all_contributors)
print("-------------------%d" %count)



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