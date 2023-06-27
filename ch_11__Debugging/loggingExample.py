#! python3

# factorialLog.py

###                                                      Using the logging Module

import logging
from pathlib import Path

p = Path(__file__)
base_dir = p.resolve().parent
destination_dir = p.resolve().parent / 'loggingFile_Folder'

# Create new folder
destination_dir.mkdir(parents=True, exist_ok=True)  
# Save log to file
logging.basicConfig(filename=str(destination_dir / 'debug.txt'), level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) # Disable Logging
logging.debug('Start of program')

def factorial(n):
    logging.debug(f'Start of factorial {n}')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.info(f'End of factorial {n}')
    return total

print(factorial(5))
logging.debug('End of program')



