#! python3


#######
#######
#                Selective Copy
#######
#######
#                Write a program that walks through a folder tree and searches for files with
#                a certain file extension (such as .pdf or .jpg).
#                Copy these files from whatever location they are in to a new folder.
#######
#######


import zipfile, shutil, os
from pathlib import Path


# C:\Users\blake\Documents\PYTHON_Scripting\Automate_the_Boring_Stuff\ch10__Organizing Files\ch10_Projects

# userInput = input("Please paste Absolute File Path you want to Search: ")

copyPath_01 =  os.path.abspath(r"C:\Users\blake\Documents\PYTHON_Scripting\Automate_the_Boring_Stuff\ch10__Organizing Files\ch10_Projects\selectiveCopy\Copy_From_Me") 

parent_path = os.path.dirname(copyPath_01)
pastePath_01 = os.path.join(parent_path, 'Paste_To_Here')


def selectiveCopy(copyPath, pastePath):


    ##
    ###     Walk to find .jpg OR .jpeg
    ##
    for dirpath, dirnames, filenames in os.walk(copyPath):

        # Get relative paths
        relative_path = os.path.relpath(dirpath, copyPath)

        # Setup Path for sub directories
        destination_dirnames = os.path.join(pastePath, relative_path)
        if not os.path.exists(destination_dirnames):
            os.makedirs(destination_dirnames)



        for filename in filenames:
            if any(filename.endswith(myExtensions) for myExtensions in ['.jpg', '.jpeg']):
                print(f"FILE INSIDE {dirpath} : {filename}")
                print(f"{filename} pasted into {pastePath} \n")

                # Copy selected Files into Destination Sub Directories
                shutil.copy(os.path.join(dirpath, filename), destination_dirnames)


selectiveCopy(copyPath_01, pastePath_01)







####################
####################

# ##
# ###     FULL OS PATH WALK
# ##
# for dirpath, dirnames, filenames in os.walk(base_path):
#     print(f"Current Folder {dirpath}")
    
#     for subfolder in dirnames:
#         print(f"SUBFOLDER OF {dirpath} : {subfolder}")

#     for filename in filenames:
#         print(f"FILE INSIDE {dirpath} : {filename}")
#     print('\n')