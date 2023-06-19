#! python3

import zipfile, shutil, os
from pathlib import Path

p = Path(__file__)

base_dir = p.resolve().parent
source_dir = p.resolve().parent / 'Source'
destination_dir = p.resolve().parent / 'Destination'

##
### Copying and Moving Files
##

# shutil.copy(source_dir / 'copy_me.txt', destination_dir / 'copy_me_renamed.txt')

# shutil.copytree(source_dir, p.resolve().parent / 'Source_Backup')

# shutil.move(source_dir / 'move_me.txt', destination_dir)

##
### Walking a Directory Tree
##

for dirpath, dirnames, filenames in os.walk(base_dir):
    print(f"Current Folder {dirpath}")

    for subfolder in dirnames:
        print(f"SUBFOLDER OF {dirpath} : {subfolder}")

    for filename in filenames:
        print(f"FILE INSIDE {dirpath} : {filename}")
    print('\n')

##
### Compressing Files
##

# # print(p)

# exampleCompression = zipfile.ZipFile(base_dir / 'example_compression.zip')

# # print(exampleCompression)

# print(exampleCompression.namelist())

# spamInfo = exampleCompression.getinfo('example_compression/spam.txt')
# print(spamInfo.file_size)
# print(spamInfo.compress_size)

# print(f'Compressed File is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller')

# exampleCompression.extractall(base_dir / 'example_compression_extraction')
# exampleCompression.close()