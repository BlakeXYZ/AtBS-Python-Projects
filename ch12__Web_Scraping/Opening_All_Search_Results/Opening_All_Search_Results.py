#! python3

### Opening All Search Results
# 1. Gets search keywords from the command line arguments
# 2. Retrieves the search results page
# 3. Opens a browser tab for each result

# This means your code will need to do the following:
# 1. Read the command line arguments from sys.argv.
# 2. Fetch the search result page with the requests module.
# 3. Find the links to each search result.
# 4. Call the webbrowser.open() function to open the web browser.
###
###

import sys, logging, webbrowser, requests, bs4

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) # Disable Logging
logging.debug('Start of program')

# searchKeywords = input('Search Keywords: ')
searchKeywords = 'howdy'

res = requests.get('https://pypi.org/search/?q=' + ''.join(searchKeywords))
logging.debug(res.url)

try:
    res.raise_for_status() # will raise an exception if error downloading file, will do nothing if download successful
except Exception as exc:
    print('There was a problem: %s' % (exc))


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElements = soup.select('.package-snippet')

# Open a browser tab for each result.
print(len(linkElements))

numOpen = min(3, len(linkElements))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElements[i].get('href')

    webbrowser.open(urlToOpen)
    print(f'Opening {urlToOpen}')





