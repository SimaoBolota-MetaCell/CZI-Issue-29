from githubInfo import *
from htmlScraper import *

# Metadata in the config file:

# - Link to source code

# -  Summary Sentence (fallback)
# - Intro paragraph (fallback)
# - Intro video or screenshot (fallback)
# - Usage (fallback)
# - Author (fallback)
# - link to support channels (fallback)
# - link to bug tracker (fallback)


repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'


git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(repo_path)
# get the current GitHub Repository README.md link, in which the search for citation will happen
README_LINK = git_repo_link + '/blob/%s/README.md'%(git_base_branch)

print(git_repo_link)

SET_UP_CFG_LINK = git_repo_link + '/blob/%s/setup.cfg'%(git_base_branch)

print(SET_UP_CFG_LINK)


soup = get_html(SET_UP_CFG_LINK)

scraped_text = soup.find_all("table", {'class': 'highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file'})
scraped_text = str(scraped_text)
scraped_text = strip_tags(scraped_text)

print(scraped_text)


SOURCE_CODE_PATTERN = '(?:Source\sCode\s\=\s)(.*?)(?=\s)'

source_code_data = re.findall(SOURCE_CODE_PATTERN, scraped_text, flags=re.DOTALL)

print(source_code_data)