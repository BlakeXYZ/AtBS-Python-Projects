#! python3

### Download XKCD Comics
# 1. Loads the XKCD home page
# 2. Saves the comic image on that page
# 3. Follows the Previous Comic link
# 4. Repeats until it reaches the first comic

# This means your code will need to do the following:
# 1. Download pages with the requests module.
# 2. Find the URL of the comic image for a page using Beautiful Soup.
# 3. Download and save the comic image to the hard drive with iter_content().
# 4. Find the URL of the Previous Comic link, and repeat

import logging, os, bs4, requests, sys, subprocess
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # Disable Logging
logging.debug('Start of program')

p = Path(__file__)
base_dir = p.resolve().parent
destination_dir = p.resolve().parent / 'XKCD Downloads Folder'

destination_dir.mkdir(parents=True, exist_ok=True)              # Store comics inside destination dir

for comicNum in range(1,10):

    url = f'https://xkcd.com/{comicNum}/'                                       # starting URL

    # Download the page.
    req = requests.get(url)
    logging.debug(req.url)

    try:
        req.raise_for_status() # will raise an exception if error downloading file, will do nothing if download successful
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    # TODO: Find the URL of the comic image.
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    imgElements =  soup.select('#comic img')

    

    if imgElements == []:
        print('Could Not Find Comic Image')
    else:
        imgURL = 'https:' + imgElements[0].get('src')
        # Download the image.
        req = requests.get(imgURL)
        req.raise_for_status() # will raise an exception if error downloading file, will do nothing if download successful

        print(f'Saving Image File: {imgURL}')

        # Save the image.
        imgFile = open(os.path.join(destination_dir, os.path.basename(imgURL)), 'wb')
        #  iter_content method ensures that the requests module doesn’t eat up too much memory even if you download massive files
        for chunk in req.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()

## Open File Explorer Path
# Determine the operating system
if sys.platform.startswith('win'):
    # For Windows
    subprocess.Popen(['explorer', base_dir])   


print('Done.')



