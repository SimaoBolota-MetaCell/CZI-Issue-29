from githubInfo import *
from htmlScraper import *


repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/Issue29/CZI-Issue-29'


git_repo_username,git_repo_name, git_repo_link,git_base_branch = getGitInfo(repo_path)


NAPARI_DESCRIPTION_LINK = git_repo_link + '/blob/%s/.napari-hub/DESCRIPTION.md'%(git_base_branch)


napari_description_soup = get_html(NAPARI_DESCRIPTION_LINK)

# print(napari_description_soup)



napari_description_scraped_text = napari_description_soup.find("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'})
# napari_description_scraped_text = str(napari_description_scraped_text)
# napari_description_scraped_text = strip_tags(napari_description_scraped_text)
print(napari_description_scraped_text)


images = 0
for tag in napari_description_soup.find_all("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'}):
    for anchor in tag.find_all('img'):
        if (bool(anchor)):
            images += + 1

print(images)

video = 0
for tag in napari_description_soup.find_all("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'}):
    for anchor in tag.find_all('video'):
        if (bool(anchor)):
            video += + 1

print(video)

usage = False
for tag in napari_description_soup.find_all("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'}):
    for anchor in tag.find_all("a", {'href':'#usage'}):
        if (bool(anchor)):
            usage = True

print(usage)


intro_paragraph_check = False
for tag in napari_description_soup.find_all("div", {'class': 'Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0'}):
    for anchor in tag.select_one('h2').find_all_previous('p', {'dir':'auto'}):
        if (bool(anchor)):
            anchor = str(anchor)
            anchor = strip_tags(anchor)
            if(len(anchor) > 0):
                intro_paragraph_check = True

print(intro_paragraph_check)


# possible_intro_paragraph = link_data_soup.select_one('h2').find_all_previous('p', {'dir':'auto'})
#         actual_text_in_p_count = 0
#         for intro_paragraph in possible_intro_paragraph:
#             if(bool(intro_paragraph.text)):
#                 actual_text_in_p_count += + 1
#         if actual_text_in_p_count > 0:
#             intro_paragraph_check = True
#         else:
#             intro_paragraph_check = False
