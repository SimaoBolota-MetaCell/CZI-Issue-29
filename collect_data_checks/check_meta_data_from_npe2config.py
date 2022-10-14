from .githubInfo import *
from .htmlScraper import *


repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'

NPE2_DISPLAY_NAME_PATTERN = '(?:\sname\:\s)(.*?)(?=\s\n)'


def name_metadata_npe2file(path):
    git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(path)

    NAPARI_NPE2_LINK = git_repo_link + '/blob/%s/napari.yaml'%(git_base_branch)

    napari_npe2_soup = get_html(NAPARI_NPE2_LINK)   
    npe2_scraped_text = napari_npe2_soup.find_all("table", {'class': 'highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file'})
    npe2_scraped_text = str(npe2_scraped_text)
    npe2_scraped_text = strip_tags(npe2_scraped_text)

    display_name_data = re.findall(NPE2_DISPLAY_NAME_PATTERN, npe2_scraped_text, flags=re.DOTALL)
    return bool(display_name_data)

x = name_metadata_npe2file(repo_path)
# print(x)