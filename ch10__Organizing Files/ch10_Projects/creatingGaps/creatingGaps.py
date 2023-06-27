#! python3

'''
Duplicate working folder
Walks through folder that contains given Prefix (ex: spam in spam001)
And inserts gap in selected spot

program that can insert gaps into numbered files so that a new file can be added
'''

import os, shutil, re
from pathlib import Path

directory_to_fix = r'C:\Users\blake\Documents\PYTHON_Scripting\Automate_the_Boring_Stuff\ch10__Organizing Files\ch10_Projects\creatingGaps\No_Gaps_Folder'
my_new_directory = 'Gaps_Created_Folder'
my_gap_index = 2
my_size_of_gap = 47

def creating_gaps(directory, new_directory, gap_index, size_of_gap):

    base_dir = os.path.abspath(directory)
    parent_dir = os.path.dirname(directory)
    destination_dir = os.path.join(parent_dir, new_directory)

    if os.path.exists(destination_dir): ####### TEMP FOR DEBUGGING
        shutil.rmtree(destination_dir)  # Delete the existing destination directory
    shutil.copytree(base_dir, destination_dir)   

    files_original = []
    files_without_suffix = [] 

    for dirpath, dirnames, filenames in os.walk(destination_dir):
        # Only explore direct files in destination_dir
        # Remove subdirectories from dirnames to prevent traversal
        dirnames.clear()

        for filename in filenames:
            # Store Orignal File Names in List to Pick up later
            files_original.append(filename)

            # searching for this pattern inside 'filename' string
            match = re.search(r'(spam).*?\.txt$', filename)
            if match:
                files_without_suffix.append(match.group(1))

    print(f'Adding gap of {size_of_gap} after {files_original[gap_index-1]}')        

    # Iterate over the range of indices in reverse order, starting from `len(files_without_suffix)` and ending at `gap_index+1`
    for index in range(len(files_without_suffix), gap_index, -1):
        
        # Get the file name from `files_without_suffix` at the current index
        file_name = files_without_suffix[index-1] 

        # Calculate the new index by adding the `size_of_gap` to the current index
        new_index = index + size_of_gap 

        new_fileName = f'{file_name}{new_index:03d}.txt'
        old_filePath = os.path.join(destination_dir, files_original[index-1])
        new_filePath = os.path.join(destination_dir, new_fileName)
        os.rename(old_filePath, new_filePath)

        print(f'{files_original[index-1]} has been renamed to {new_fileName}')

creating_gaps(directory_to_fix, my_new_directory, my_gap_index, my_size_of_gap)