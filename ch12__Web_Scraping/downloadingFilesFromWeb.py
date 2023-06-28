#! python3

### Using requests module to download files from web
###
###

# Summary 
# 1. Call requests.get() to download the file.
# 2. Call open() with 'wb' to create a new file in write binary mode.
# 3. Loop over the Response object’s iter_content() method.
# 4. Call write() on each iteration to write the content to the file.
# 5. Call close() to close the file

# print(type(res))
# print(res.status_code == requests.codes.ok)
# print(len(res.text))
# print(res.text[:250])

import requests, sys, subprocess
from pathlib import Path

p = Path(__file__)
base_dir = p.resolve().parent
destination_dir = p.resolve().parent / 'downloadingFilesFromWeb_Folder'

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    res.raise_for_status() # will raise an exception if error downloading file, will do nothing if download successful
except Exception as exc:
    print('There was a problem: %s' % (exc))

destination_dir.mkdir(parents=True, exist_ok=True)  
saveText = open(destination_dir / 'saveText.txt', 'wb') # Must use 'wb' as 2nd arg to write Binary Data to maintain Unicode Encoding of Text

#  iter_content method ensures that the requests module doesn’t eat up too much memory even if you download massive files
for chunk in res.iter_content(100000):
    saveText.write(chunk)

saveText.close()
   
## Open File Explorer Path
# Determine the operating system
if sys.platform.startswith('win'):
    # For Windows
    subprocess.Popen(['explorer', base_dir])   

