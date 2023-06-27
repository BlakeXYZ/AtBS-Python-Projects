#! python3
# mclip.py - A multi-clipboard program.

import sys, pyperclip

TEXT = {
    'agree' : "Yes, I agree, that sounds fine to me",
    'busy' : "Sorry dude I'm pretty busy this weekend",
    'upsell' : "We would greatly appreciate your patronage, sire"

}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Successfully Copied ' + keyphrase + ' phrase. Which equals: ' + TEXT[keyphrase])
else:
    print('There is no phrase for ' + keyphrase)


