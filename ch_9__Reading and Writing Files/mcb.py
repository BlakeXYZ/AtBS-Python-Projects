#! python3

# mcb.pyw - Saves and Loads Pieces of Text to the Clipboard

help = """
ch9_mcb save <keyword> -    Saves Clipboard to Keyword
ch9_mcb <keyword> -         Loads Keyword to Clipboard
ch9_mcb list -              Loads All Keywords to Clipboard
ch9_mcb delete <keyword> -  Delete Saved Keyword
ch9_mcb deleteAll -         Deletes all Keywords
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(f'Successfully Saved: {sys.argv[2]}' )

# List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(f'Your Saved Keywords: {list(mcbShelf.keys())}' )

    if sys.argv[1] == 'deleteAll':
        print(f'Deleted All: {list(mcbShelf.keys())}' )  
        for key in mcbShelf:
            del mcbShelf[key] 

    if sys.argv[1] == 'help':
        print(help)  

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

 # Delete clipboard content.
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete': 
    key = sys.argv[2]
    if key in mcbShelf:
        del mcbShelf[key]
        print(f'Successfully deleted: {key}')
    else:
        print(f'Key not found: {key}')

mcbShelf.close()