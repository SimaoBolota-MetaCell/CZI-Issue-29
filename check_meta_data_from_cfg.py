from githubInfo import *
from htmlScraper import *

# Metadata in the config file:

# -  Summary Sentence (fallback)
# - Intro paragraph (fallback)
# - Intro video or screenshot (fallback)

# - Usage (fallback)

# - Link to source code
# - Author (fallback)
# - link to support channels (fallback)
# - link to bug tracker (fallback)


repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'


git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(repo_path)

print(git_repo_link)

SET_UP_CFG_LINK = git_repo_link + '/blob/%s/setup.cfg'%(git_base_branch)

print(SET_UP_CFG_LINK)


soup = get_html(SET_UP_CFG_LINK)

scraped_text = soup.find_all("table", {'class': 'highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file'})
scraped_text = str(scraped_text)
scraped_text = strip_tags(scraped_text)

print(scraped_text)

print('----------------------------------------------------------------')

PYCFG_DISPLAY_NAME_PATTERN = '(?:name\s\=\s)(.*?)(?=\s\n)'
PYCFG_SUMMARY_SENTENCE_PATTERN = '(?=\sdescription\s\=\s)(.*?)(?=\s\n)'
PYCFG_LONG_DESCRIPTION_PATTERN = '(?:long_description\s\=\s)(.*?)(?=\s\n)'
PYCFG_SOURCE_CODE_PATTERN = '(?:Source\sCode\s\=\s)(.*?)(?=\s)'
PYCFG_AUTHOR_PATTERN = '(?:author\s\=\s)(.*?)(?=\s\n)'
PYCFG_BUG_TRACKER_PATTERN = '(?:Bug\sTracker\s\=\s)(.*?)(?=\s)'
PYCFG_USER_SUPPORT_PATTERN = '(?:User\sSupport\s\=\s)(.*?)(?=\s)'

display_name_data = re.findall(PYCFG_DISPLAY_NAME_PATTERN, scraped_text, flags=re.DOTALL)
long_description_data = re.findall(PYCFG_LONG_DESCRIPTION_PATTERN, scraped_text, flags=re.DOTALL)
summary_sentence_data = re.findall(PYCFG_SUMMARY_SENTENCE_PATTERN, scraped_text, flags=re.DOTALL)
source_code_data = re.findall(PYCFG_SOURCE_CODE_PATTERN, scraped_text, flags=re.DOTALL)
author_data = re.findall(PYCFG_AUTHOR_PATTERN, scraped_text, flags=re.DOTALL)
bug_tracker_data = re.findall(PYCFG_BUG_TRACKER_PATTERN, scraped_text, flags=re.DOTALL)
user_support_data = re.findall(PYCFG_USER_SUPPORT_PATTERN, scraped_text, flags=re.DOTALL)

print('\n Display name ')
print(display_name_data)
print('\n Intro prarapgraph/video/screenshot/Usage ')
print(long_description_data)
print('\n Summary sentence  ')
print(summary_sentence_data)
print('\n Source code link ')
print(source_code_data)
print('\n Author')
print(author_data)
print('\n Bug Tracker Link ')
print(bug_tracker_data)
print('\n Support channels link ')
print(user_support_data)


for data in long_description_data:
   
    FILE_IN_LONG_DESCRIPTION_PATTERN = '(?:file\:\s)(.*?)(?=\s)'
    long_description_file = re.findall(FILE_IN_LONG_DESCRIPTION_PATTERN, data, flags=re.DOTALL)
    
    if bool(long_description_file):
       
        long_description_file = ''.join(long_description_file)
        LONG_DESCRIPTION_LINK = git_repo_link + '#%s'%(long_description_file)
        print('\nLink to the long description file:')
        print(LONG_DESCRIPTION_LINK)
        long_description_soup = get_html(LONG_DESCRIPTION_LINK)
        # print(long_description_soup)

        link_data_soup = long_description_soup.find_all("div",{'data-tagsearch-path': long_description_file})
        link_data_soup = link_data_soup[0]
        # print(link_data_soup)

        video_data = link_data_soup.find_all("video")
        print('\nVideo data count:')
        print(len(video_data))

        screenshot_data = link_data_soup.find_all("img")
        print('\nScreenshot data count:')
        print(len(screenshot_data))
