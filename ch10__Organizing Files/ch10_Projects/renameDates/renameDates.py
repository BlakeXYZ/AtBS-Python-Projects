#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re
from pathlib import Path

p = Path(__file__)

base_dir = p.resolve().parent
rename_dir = p.resolve().parent / 'Rename_These_Dates'

# Create a regex that can identify the text pattern of American-style dates

americanDatePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-         # one or two digits for the month
    ((0|1|2|3)?\d)-     # one or two digits for the day
    ((19|20)\d\d)       # four digits for the year
    (.*?)$              # all text after the date 
    """, re.VERBOSE 
)

print(f'total file count inside /{rename_dir.name}: {len(os.listdir(rename_dir))}')
# Loop over the files in the working directory.
for americanFilename in os.listdir(rename_dir):
    mo = americanDatePattern.search(americanFilename)
# Skip files without a date.
    if mo == None:
        continue
# Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# TODO: Form the European-style filename. DD-MM-YYYY

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
# TODO: Get the full, absolute file paths.
    os.makedirs(rename_dir / 'euro_dates', exist_ok=True)


    americanFilename = os.path.join(rename_dir, americanFilename)
    euroFilename = os.path.join(rename_dir / 'euro_dates', euroFilename)

    print(americanFilename)
    print(euroFilename)
    shutil.move(americanFilename, euroFilename)


