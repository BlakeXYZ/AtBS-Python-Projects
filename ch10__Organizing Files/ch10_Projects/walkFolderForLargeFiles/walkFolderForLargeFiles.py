#! python3

'''

A program that walks through a folder tree and searches for exceptionally large files or folders
(Remember that to get a files size, you can use os.path.getsize() from the os module.) 
Print these files with their absolute path to the screen.

'''

import os


userInput = input("Please paste Absolute File Path you want to Search: ")



pathToWalk = os.path.abspath(userInput)



def showFolderSizes (basePath):

    for dirpath, dirnames, filenames in os.walk(basePath):
        byte_size = round(0, 2)

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            byte_size += os.path.getsize(file_path)
            
        
        kb_size = round(byte_size / 1024, 2)
        mb_size = round(kb_size / 1024, 2)
        gb_size = round(mb_size / 1024, 2)

        if gb_size >= 1:
            print(f"{dirpath}: {gb_size} gb")
        elif mb_size >= 1:
            # print(f"{dirpath}: {mb_size} mb")
            continue
        elif kb_size >= 1:
            # print(f"{dirpath}: {kb_size} kb")
            continue
        else:
            # print(f"{dirpath}: {byte_size} bytes")
            continue

        # print('\n')

def get_folder_size(folder_path):
    total_size = 0


    for path, dirs, files in os.walk(folder_path):
        for f in files:
            file_path = os.path.join(path, f)
            total_size += os.path.getsize(file_path)



    subfolder_Dict = {}

    # Iterate over immediate subdirectories
    for dir in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, dir)

        # print(f" --- Walking: {dir} ---")
        subfolder_Size = 0

        if os.path.isdir(subfolder_path):
            for path, dirs, files in os.walk(subfolder_path):
                for f in files:
                    file_path = os.path.join(path, f)
                    subfolder_Size += os.path.getsize(file_path)


        subfolder_Size_mb = round(subfolder_Size / (1024 * 1024), 2)
        subfolder_Dict[dir] = str(subfolder_Size_mb) + ' mb'



        # print(f"Sub Size: {subfolder_Size_mb} mb")

    sorted_dict = dict(sorted(subfolder_Dict.items(), key=lambda x: float(x[1].replace(' mb', ''))))
    for key, value in sorted_dict.items():
        print (f'{key:25} : {value}')


    print(f"-- -- -- -- -- -- -- \n Total Size: {round(total_size / (1024 * 1024), 2)} mb")





showFolderSizes(pathToWalk)
#get_folder_size(pathToWalk)