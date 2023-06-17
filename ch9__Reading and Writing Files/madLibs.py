#! python3

import re, os, random
import pyinputplus as pyip

# Store User Name
user_name = pyip.inputStr('Please enter your name: ')
print(f'Welcome {user_name}, lets build a Mad Libs!')

##                                                                           Building Folder Structure
#   Get the directory path of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))
#   Create the file path
file_path = os.path.join(script_directory, 'madLibs_Sentences', 'madLibs_Sentences_MASTER.txt')

#   Open and Read File
sentences_MASTER = open(file_path, 'r')
fillMeInSentence = sentences_MASTER.read().split("\n")
#   Randomize Order
random.shuffle(fillMeInSentence)


# Find all matches and replace them in each line
regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

result = ""

for i in range(len(fillMeInSentence)):
    line = fillMeInSentence[i]
    matches = regex.findall(line)

    for match in matches:
        match = next(filter(None, match))
        user_input = input(f"Enter a {match}: ")
        line = line.replace(match, user_input, 1)
    
    fillMeInSentence[i] = line
    result += line + '\n'  # Append the modified line with a newline character

    # Continue to next Mad Libs???
    if i < len(fillMeInSentence) - 1:
        print("\n" + fillMeInSentence[i])

        while True:
            user_input = input("\nDo you want to build another Mad Libs (Y/N)?")
            if user_input.upper() == 'N' or user_input.upper() == 'Y':
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        if user_input.upper() == 'Y':
            print("\n Continuing to the next Mad Libs \n")
            continue
        elif user_input.upper() == 'N':
                break



print("Final Sentence(s):\n", result)
#   Save into new TXT file for User
file_path_to_save = os.path.join(script_directory, 'madLibs_Sentences')
user_File = open(os.path.join(file_path_to_save, f'madLibs_{user_name}.txt'), 'w')
user_File.write(result)

print(f"Your Mad Lib sentences have been saved to the directory: {file_path_to_save}")


