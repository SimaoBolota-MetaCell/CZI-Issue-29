
from githubInfo import *

import json, requests
from bs4 import BeautifulSoup

repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'


git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(repo_path)
# get the current GitHub Repository README.md link, in which the search for citation will happen
README_LINK = git_repo_link + '/blob/%s/README.md'%(git_base_branch)


source_code_link = git_repo_link 
print(source_code_link)





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


contributor_usernames = [ 'SimaoBolota','SimaoBolota-MetaCell']

real_username = []

for contributor_username in contributor_usernames:
    github_html = requests.get(f'https://github.com/{contributor_username}').text
    soup = BeautifulSoup(github_html, "html.parser")
    avatar_block = soup.find_all('form',{'class':'ajax-pagination-form js-ajax-pagination js-show-more-timeline-form col-lg-10 col-12'})
    paragraphs = []
    for x in avatar_block:
     paragraphs.append(str(x))
    for paragraph in paragraphs:
        data_title = re.findall('(?:data-title\=\")(.*?)(?=\")', paragraph, flags=re.DOTALL)
    for data in data_title:
        found_data = re.findall('(?:\()(.*?)(?=\))', data, flags=re.DOTALL)
        if(len(found_data) == 0):
            found_data = ['N/A']
        real_username = real_username + found_data
print(real_username)


from rich import print


from rich.console import Console
from rich.table import Table

checked_element = u'\u2713'
non_checked_element = u'\u2717'

checked_style = 'green'
unchecked_style = 'red'


author_name_check = []
summary_sentence_check = []

if bool(real_username):
    author_name_check = checked_element
    author_name_column_style = checked_style
else:
    author_name_check = non_checked_element
    author_name_column_style = unchecked_style


if bool(source_code_link):
    sc_link_check = checked_element
    sc_link_column_style = checked_style
else:
    sc_link_check = non_checked_element
    sc_link_column_style = unchecked_style

table = Table(title="Napari Documentation Checklist")

table.add_column("Author Names", justify="right", style=author_name_column_style, no_wrap=True)
table.add_column("Summary Sentence", justify="right", style="magenta")
table.add_column("Intro Paragraph", justify="right", style="green")
table.add_column("Intro Video/Screenshot", justify="right", style="green")
table.add_column("Usage Overview", justify="right", style="green")
table.add_column("Source Code Link", justify="right", style=sc_link_column_style)
table.add_column("Support Channel Link", justify="right", style="green")
table.add_column("Issue Submission Link", justify="right", style="green")
table.add_column("Display Name", justify="right", style="green")

table.add_row(author_name_check, "Star Wars: The Rise of Skywalker", "$952,110,690", "", "",sc_link_check ,"" )

console = Console()
console.print(table, justify="center")



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