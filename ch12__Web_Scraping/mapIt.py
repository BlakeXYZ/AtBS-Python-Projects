#! python3

### mapIt.py - Launches a map in the browser using an address from the command line or clipboard
###
###

import sys, pyperclip, webbrowser, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) # Disable Logging

logging.debug('Start of program')

if len(sys.argv) > 1:
    # Get Address From Commandline
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


logging.debug(f'https://www.google.com/maps/place/{address}')
webbrowser.open(f'https://www.google.com/maps/place/{address}')
