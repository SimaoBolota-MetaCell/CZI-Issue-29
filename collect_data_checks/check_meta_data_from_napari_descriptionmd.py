from .githubInfo import *
from .htmlScraper import *

def description_soup(path):
    git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(repo_path)
    NAPARI_DESCRIPTION_LINK = git_repo_link + '/blob/%s/.napari-hub/DESCRIPTION.md'%(git_base_branch)

    return get_html(NAPARI_DESCRIPTION_LINK)


def screenshot_metadata_descriptionfile(soup):

    images = 0
    image_check = False
    for tag in soup.find_all("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'}):
        for anchor in tag.find_all('img'):
            if (bool(anchor)):
                images += 1
    if (images>0):
        image_check = True
    return(image_check)



def video_metadata_descriptionfile(soup):
    
    video = 0
    video_check = False
    for tag in soup.find_all("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'}):
        for anchor in tag.find_all('video'):
            if (bool(anchor)):
                video += 1
    if(video>0):
        video_check = True
    return(video_check)



def usage_metadata_descriptionfile(soup):

    usage = False
    for tag in soup.find_all("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'}):
        for anchor in tag.find_all("a", {'href':'#usage'}):
            if (bool(anchor)):
                usage = True
    return(usage)



def intro_metadata_descriptionfile(soup):

    intro_paragraph_check = False
    for tag in soup.find_all("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'}):
        for anchor in tag.select_one('h2').find_all_previous('p', {'dir':'auto'}):
            if (bool(anchor)):
                anchor = str(anchor)
                anchor = strip_tags(anchor)
                if(len(anchor) > 0):
                    intro_paragraph_check = True
    return(intro_paragraph_check)


repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'

x_soup = description_soup(repo_path)
y = screenshot_metadata_descriptionfile(x_soup)
# print(y)


z = video_metadata_descriptionfile(x_soup)
# print(z)


c = usage_metadata_descriptionfile(x_soup)
# print(c)


d = intro_metadata_descriptionfile(x_soup)
# print(d)