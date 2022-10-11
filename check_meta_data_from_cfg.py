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


SET_UP_CFG_LINK = git_repo_link + '/blob/%s/setup.cfg'%(git_base_branch)



soup = get_html(SET_UP_CFG_LINK)

setup_cfg_scraped_text = soup.find_all("table", {'class': 'highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file'})
setup_cfg_scraped_text = str(setup_cfg_scraped_text)
setup_cfg_scraped_text = strip_tags(setup_cfg_scraped_text)


PYCFG_DISPLAY_NAME_PATTERN = '(?:name\s\=\s)(.*?)(?=\s\n)'
PYCFG_SUMMARY_SENTENCE_PATTERN = '(?:\sdescription\s\=\s)(.*?)(?=\s\n)'
PYCFG_LONG_DESCRIPTION_PATTERN = '(?:long_description\s\=\s)(.*?)(?=\s\n)'
PYCFG_SOURCE_CODE_PATTERN = '(?:Source\sCode\s\=\s)(.*?)(?=\s)'
PYCFG_AUTHOR_PATTERN = '(?:author\s\=\s)(.*?)(?=\s\n)'
PYCFG_BUG_TRACKER_PATTERN = '(?:Bug\sTracker\s\=\s)(.*?)(?=\s)'
PYCFG_USER_SUPPORT_PATTERN = '(?:User\sSupport\s\=\s)(.*?)(?=\s)'

display_name_data = re.findall(PYCFG_DISPLAY_NAME_PATTERN, setup_cfg_scraped_text, flags=re.DOTALL)
long_description_data = re.findall(PYCFG_LONG_DESCRIPTION_PATTERN, setup_cfg_scraped_text, flags=re.DOTALL)
summary_sentence_data = re.findall(PYCFG_SUMMARY_SENTENCE_PATTERN, setup_cfg_scraped_text, flags=re.DOTALL)
source_code_data = re.findall(PYCFG_SOURCE_CODE_PATTERN, setup_cfg_scraped_text, flags=re.DOTALL)
author_data = re.findall(PYCFG_AUTHOR_PATTERN, setup_cfg_scraped_text, flags=re.DOTALL)
bug_tracker_data = re.findall(PYCFG_BUG_TRACKER_PATTERN, setup_cfg_scraped_text, flags=re.DOTALL)
user_support_data = re.findall(PYCFG_USER_SUPPORT_PATTERN, setup_cfg_scraped_text, flags=re.DOTALL)

print('\n Display name ')
if(bool(display_name_data)):
    display_name_check = True
else:
    display_name_check = False
print(display_name_check)


print('\n Summary sentence  ')
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

print('\n Intro prarapgraph/video/screenshot/Usage location:')
print(long_description_data)
print('checking long description file...')
for data in long_description_data:
   
    FILE_IN_LONG_DESCRIPTION_PATTERN = '(?:file\:\s)(.*?)(?=\s)'
    long_description_file = re.findall(FILE_IN_LONG_DESCRIPTION_PATTERN, data, flags=re.DOTALL)
    
    if bool(long_description_file):
       
        long_description_file = ''.join(long_description_file)
        LONG_DESCRIPTION_LINK = git_repo_link + '#%s'%(long_description_file)
        print('\nLink to the long description file:')
        print(LONG_DESCRIPTION_LINK)
        long_description_soup = get_html(LONG_DESCRIPTION_LINK)

        link_data_soup = long_description_soup.find_all("article",{'class': 'markdown-body entry-content container-lg'})
        link_data_soup = link_data_soup[0]

        video_data = link_data_soup.find_all("video")
        if len(video_data)>0:
            intro_video_check = True
        else:
            intro_video_check = False
        print('\nIntro Video data')
        print(intro_video_check)

        screenshot_data = link_data_soup.find_all("img")
        if len(screenshot_data)>0:
            intro_screenshot_check = True
        else:
            intro_screenshot_check = False
        print('\nIntro Screenshot data')
        print(intro_screenshot_check)

        
        usage_data = link_data_soup.find_all("a", {'href':'#usage'})
        print('\nUsage data')
        print(bool(usage_data))

        
        possible_intro_paragraph = link_data_soup.select_one('h2').find_all_previous('p', {'dir':'auto'})
        actual_text_in_p_count = 0
        for intro_paragraph in possible_intro_paragraph:
            if(bool(intro_paragraph.text)):
                actual_text_in_p_count += + 1
        if actual_text_in_p_count > 0:
            intro_paragraph_check = True
        else:
            intro_paragraph_check = False
        
        print('\nIntro Paragraph')
        print(intro_paragraph_check)


        
