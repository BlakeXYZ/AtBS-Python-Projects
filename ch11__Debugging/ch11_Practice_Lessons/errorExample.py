#! python3

###                                                      Getting the Traceback as a String
import traceback
from pathlib import Path

p = Path(__file__)
base_dir = p.resolve().parent
destination_dir = p.resolve().parent / 'errorFile_Folder'

try:
    raise Exception('This is the Error Message!!!')
except:
    destination_dir.mkdir(parents=True, exist_ok=True)  # Create the new folder
    error_file_path = destination_dir / 'errorInfo.txt'
    errorFile = open(destination_dir / error_file_path, 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print(f'The traceback info was written to {error_file_path.relative_to(base_dir)}')



