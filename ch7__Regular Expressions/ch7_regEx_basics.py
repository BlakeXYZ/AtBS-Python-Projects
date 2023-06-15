#! python3
# Regular Expression Basics

import re

textInput = 'My number is 415-555-4242.'

# Regular expression to search for phone number
phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

# Search for phone number in input text
match = phoneNumberRegex.search(textInput)

# Print the phone number as a string if found
if match:
    print(str(match.group(1)))
    print(str(match.group(2)))
    print(str(match.group(0)))

#
#
#
#

batTextInput = 'batman is getting the batmobile with the batcat'

batRegex = re.compile(r'bat(man|mobile|woman|kiddo|cat)')

matches = batRegex.findall(batTextInput)

if matches:
    for match in matches:
        print('bat' + match)

#
#
#
#

christmasTextInput = ('12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge in a pear tree yippee yahoo yay')

regex = re.compile(r'(\d+)\s+(\S.*?)(?=\s*\d|$)')

matches = regex.findall(christmasTextInput)

if matches:
    for match in matches:
        print(match)


#
#
#
#
