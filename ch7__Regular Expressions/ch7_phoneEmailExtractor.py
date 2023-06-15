#! python3
# Project: Phone Number and Email Address Extractor

import sys, pyperclip, re

#       OVERVIEW
# 1. Get the text off the clipboard.
# 2. Find all phone numbers and email addresses in the text.
# 3. Paste them onto the clipboard




# 1. Use the pyperclip module to copy and paste strings.

# Copy a string to clipboard
textInput = pyperclip.paste()

# print(textInput)



# 2. Create two regexes, one for matching phone numbers and the other for matching email addresses.

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                  # area code
        (\s|-|\.)?                          # separator
        (\d{3})                             # first 3 digits
        (\s|-|\.)                           # separator
        (\d{4})                             # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
        )''', re.VERBOSE)


# TODO: Create email regex.

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+                   # username
        @                                   # @ symbol
        [a-zA-Z0-9.-]+                      # domain name
        (\.[a-zA-Z]{2,4})                   # dot-something
        )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

phoneMatch = phoneRegex.findall(textInput)
emailMatch = emailRegex.findall(textInput)

nameAndNumber = []
if not phoneMatch and not emailMatch:
    print("No phone numbers or email addresses found.")
else:
    for match in phoneMatch:
        nameAndNumber.append(''.join(match[0]))
    for match in emailMatch:
        nameAndNumber.append(''.join(match[0]))

print('\n'.join(nameAndNumber))
pyperclip.copy('\n'.join(nameAndNumber))
