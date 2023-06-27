#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste
# text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'

# Separate Lines and Add Stars
lines = text.split('\n')

for i in range (len(lines)):
    lines[i] = '* ' + lines[i]


textBulleted = '\n'.join(lines)

print(textBulleted)
pyperclip.copy(textBulleted)
