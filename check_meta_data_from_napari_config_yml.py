from githubInfo import *
from htmlScraper import *


repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'


git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(repo_path)


NAPARI_CFG_LINK = git_repo_link + '/blob/%s/.napari-hub/config.yml'%(git_base_branch)


napari_cfg_soup = get_html(NAPARI_CFG_LINK)


napari_cfg_scraped_text = napari_cfg_soup.find_all("table", {'class': 'highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file'})
napari_cfg_scraped_text = str(napari_cfg_scraped_text)
napari_cfg_scraped_text = strip_tags(napari_cfg_scraped_text)
print(napari_cfg_scraped_text)

NAPARI_CFG_SUMMARY_SENTENCE_PATTERN = '(?:\sdescription\:\s)(.*?)(?=\s\n)'
NAPARI_CFG_SOURCE_CODE_PATTERN = '(?:Source\sCode\:\s)(.*?)(?=\s)'
NAPARI_CFG_AUTHOR_PATTERN = '(?:author\:\s)(.*?)(?=\s\n)'
NAPARI_CFG_BUG_TRACKER_PATTERN = '(?:Bug\sTracker\:\s)(.*?)(?=\s)'
NAPARI_CFG_REPORT_ISSUES_PATTERN = '(?:Report\sIssues\:\s)(.*?)(?=\s)'
NAPARI_CFG_USER_SUPPORT_PATTERN = '(?:User\sSupport\:\s)(.*?)(?=\s)'

summary_sentence_data = re.findall(NAPARI_CFG_SUMMARY_SENTENCE_PATTERN, napari_cfg_scraped_text, flags=re.DOTALL)
source_code_data = re.findall(NAPARI_CFG_SOURCE_CODE_PATTERN, napari_cfg_scraped_text, flags=re.DOTALL)
author_data = re.findall(NAPARI_CFG_AUTHOR_PATTERN, napari_cfg_scraped_text, flags=re.DOTALL)
user_support_data = re.findall(NAPARI_CFG_USER_SUPPORT_PATTERN, napari_cfg_scraped_text, flags=re.DOTALL)

if (bool(re.findall(NAPARI_CFG_BUG_TRACKER_PATTERN, napari_cfg_scraped_text, flags=re.DOTALL))):
    bug_tracker_data = re.findall(NAPARI_CFG_BUG_TRACKER_PATTERN, napari_cfg_scraped_text, flags=re.DOTALL)
else:
    bug_tracker_data = re.findall(NAPARI_CFG_REPORT_ISSUES_PATTERN, napari_cfg_scraped_text, flags=re.DOTALL)



print('\n Summary Sentence ')
if(bool(summary_sentence_data)):
    summary_sentence_check = True
else:
    summary_sentence_check = False
print(summary_sentence_check)

print('\n Source code link ')
if(bool(summary_sentence_data)):
    source_code_check = True
else:
    source_code_check = False
print(source_code_check)

print('\n Author')
if(bool(author_data)):
    author_check = True
else:
    author_check = False
print(author_check)

print('\n Bug Tracker Link ')
if(bool(bug_tracker_data)):
    bug_tracker_check = True
else:
    bug_tracker_check = False
print(bug_tracker_check)

print('\n Support channels link ')
if(bool(user_support_data)):
    user_support_check = True
else:
    user_support_check = False
print(user_support_check)