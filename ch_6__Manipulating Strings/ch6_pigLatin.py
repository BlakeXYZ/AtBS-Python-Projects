#! python3
# If a word begins with a vowel, the word yay is added to the end of it. 

# If a word begins with a consonant or consonant cluster (like ch or gr), 
# that consonant or cluster is moved to the end of the word followed by ay.

# example
# Enter the English message to translate into Pig Latin:
# My name is AL SWEIGART and I am 4,000 years old.
# Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.


# submittedText = pyperclip.paste
submittedText = 'My name is AL SWEIGART and I am 4,000 years old.'

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in pig latin

for word in submittedText.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''

    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    # Make All Words Lower Case for translation
    word = word.lower()


    # Separate the consonants at the start of this word:    
    prefixConsonants = ''

    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

     # Add the Pig Latin ending to the word: 

     # If a word begins with a vowel, the word yay is added to the end of it. 

     # If a word begins with a consonant or consonant cluster (like ch or gr), 
     # that consonant or cluster is moved to the end of the word followed by ay. 
 
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word. 
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)      

print(' '.join(pigLatin))





