

Oct 10
--

Most of the documentation fields fallback to using the config.py file, so that's the first step:

<img width="626" alt="image" src="https://user-images.githubusercontent.com/99416933/194862056-7b27e45c-52c9-4caf-b625-974ed4b3a6e7.png">


For the Intro video/screenshot , Intro Paragraph and Usage - the config.py file redirects normally to the README:
- Count existent img  tag
- Count existent video tag

<img width="633" alt="image" src="https://user-images.githubusercontent.com/99416933/194862431-91bd3a90-4dcd-49e9-89bd-a21425726435.png">


**Question** - Is the task just checking for the information? Or to add it in the supposed files if not present? Why the question - some of the fields like issue links or source code or authors can be scraped from the GitHub repo

Oct 17
--

Scraped information from **config.yml** ()

Scraped information from **.napari/description.md** ()

Scraped information from **npe2 config file** ()

**Created checklist**

An element of the checklist appears as checked if any of its corresponding file locations have the expected metadata (OR statements)


Example 1 (some fields missing)

<img width="446" alt="image" src="https://user-images.githubusercontent.com/99416933/196182974-b62dbba0-f3cd-426d-b09b-bbe83f537d1b.png">

![jhrgiugwr](https://user-images.githubusercontent.com/99416933/196183498-576d7980-a93c-425a-939c-7949bf2eec6b.gif)


Example 2 
By adding a screenshot in the description.md and a CITATION.CFF file

![jiuju](https://user-images.githubusercontent.com/99416933/196184100-4fb63254-4676-4e39-b10c-e72d680f72de.gif)

<img width="459" alt="image" src="https://user-images.githubusercontent.com/99416933/196183978-cfc8dc99-2975-4c24-b965-c5ef3a336efc.png">

**Questions:**

- Should I add the CITATION.CFF to the checklist?
- The npe2 config file is the napari.yml. Does it only need to have the word napari for example env-napari-segment.yml ? or is it specifically napari.yml ?
- If there's a metadata field found but in the fallback file, should I suggest the main one? or only if nothing is found?

