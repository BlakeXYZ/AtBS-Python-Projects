#! python3

# Write a program that opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression. The results should
# be printed to the screen.
import re, os
##                                                                           Building Folder Structure
#   Get the directory path of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))
#   Create the file path
dir_path = os.path.join(script_directory, 'regex_search_folder')

# List files in the directory
files = os.listdir(dir_path)

while True:
    pattern_input = input("***\nEnter a regular expression pattern: ")
    pattern_occurred = False

    for file in files:
        file_path = os.path.join(dir_path, file)
        # print(file_path)

        # Open File and split each line
        file_open = open(file_path, 'r')
        file_line_list = file_open.read().split("\n")

        # Loop thru file_line_list and store index using enumerate
        for index, line in enumerate(file_line_list, start=1):
        # using regex, search each line using pattern input and print it out
            if re.search(pattern_input, line):
                print(f"Search Pattern '{pattern_input}' Found in...\nFile: '{file}' on Line: '{index}' = '{line}'\n")
                pattern_occurred = True 
            # matches = re.findall(pattern_input, line)
            # print(matches)

    if not pattern_occurred:
        print(f"\nNo Search Pattern '{pattern_input}' Found\n")

