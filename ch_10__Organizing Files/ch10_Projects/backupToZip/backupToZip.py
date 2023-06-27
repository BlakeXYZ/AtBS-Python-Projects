#! python3
# backupToZip.py - Copies an entire folder and its contents into 
# a ZIP file whose file name increments

import os, zipfile


def backupToZip(folder):

    folder = os.path.abspath(folder) # make sure folder is absolute
    base_dir = os.path.dirname(folder)

    ### Backup entire contents of "folder" into a ZIP file.
    ##
    ### Figure out filename code should use based on
    ### what file already exists
    ##
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        zipPath = os.path.join(base_dir, zipFilename)

        if not os.path.exists(zipPath):
            break
        number += 1

    ##
    ### Create the ZIP file.
    ##
    print(f'Creating {zipPath}...')
    backupZip = zipfile.ZipFile(zipPath, 'w')

    ##
    ### Walk the entire folder tree and compress the files in each folder.
    ##
    for folderName, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {folderName}...')
        # Add the current folder to the zip file
        relative_path = os.path.relpath(folderName, folder)
        backupZip.write(folderName, relative_path)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_' 
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up the backup ZIP files

            file_path = os.path.join(folderName, filename)
            backupZip.write(file_path, os.path.join(relative_path, filename))


    backupZip.close()
    print('Done.')


folderInput = input("Please paste Absolute File Path you want to Backup: ")
backupToZip(folderInput)


