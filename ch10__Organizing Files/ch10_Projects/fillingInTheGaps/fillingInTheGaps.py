#! python3

'''
Duplicate working folder

Walks through folder that contains given Prefix (ex: spam in spam001)
and locates any gaps in the suffix numbering.

And renames all later files to close gap.
'''

import os, shutil, re
from pathlib import Path

directory_to_fix = r"C:\Users\blake\Documents\PYTHON_Scripting\Automate_the_Boring_Stuff\ch10__Organizing Files\ch10_Projects\fillingInTheGaps\Gaps_Folder"

def filling_in_the_gaps(directory):

    base_dir = os.path.abspath(directory)
    parent_dir = os.path.dirname(directory)
    destination_dir = os.path.join(parent_dir, 'Fixed_Gaps_Folder')

    files_original = []
    files_without_suffix = []

    if os.path.exists(destination_dir): ####### TEMP FOR DEBUGGING
        shutil.rmtree(destination_dir)  # Delete the existing destination directory
    shutil.copytree(base_dir, destination_dir)

    for dirpath, dirnames, filenames in os.walk(destination_dir):
        # Only explore direct files in destination_dir
        # Remove subdirectories from dirnames to prevent traversal
        dirnames.clear()

        relative_path = os.path.relpath(dirpath, parent_dir)

        for filename in filenames:
            ## Store Orignal File Names in List to Pick up later
            files_original.append(filename)

            match = re.search(r'(spam).*?\.txt$', filename)
            if match:
                files_without_suffix.append(match.group(1))

    for index, file_name in enumerate(files_without_suffix, start=1):
        new_fileName = f'{file_name}{index:03d}.txt'
        old_filePath = os.path.join(destination_dir, files_original[index-1])
        new_filePath = os.path.join(destination_dir, new_fileName)
        os.rename(old_filePath, new_filePath)

        print(f'"{files_original[index-1]}" renamed to "{new_fileName}"\n')

filling_in_the_gaps(directory_to_fix)