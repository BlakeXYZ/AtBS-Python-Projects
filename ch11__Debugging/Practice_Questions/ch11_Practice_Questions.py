#! python3

###
### Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10 
##

# def spam(n):
#     for i in range(1, n + 1):
#         print(f'{i} spam')

#     assert i > 10, 'Spam Argument is less than 10'

# spam(5)

###
### Write an assert statement that triggers an AssertionError if var: eggs and bacon contain strings that are the same, even if
### cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
##

# def egg_bacon_assertion():
#     egg = input('egg = ')
#     bacon = input('bacon = ')

#     assert egg.lower() != bacon.lower(), f'Egg "{egg}" and Bacon "{bacon}" are the same'

#     print(f'Egg "{egg}"  and Bacon "{bacon}" are different')


# egg_bacon_assertion()   

###
### Write an assert statement that always triggers an AssertionError.
##

# def always_assert():
#     print('Hello World')
#     assert False, 'This assert always triggers'

# always_assert()

###
### What are the two lines that your program must have in order to be able to call logging.debug()?
##

# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

###
### What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
##

# import logging
# logging.basicConfig(filename=str(destination_dir / 'programLog.txt'), level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

###
### What are the five logging levels?
##

# import logging

# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()

###
### What line of code can you add to disable all logging messages in your program?
##

# logging.disable(logging.CRITICAL) # Disable ALL Logging

###
### Why is using logging messages better than using print() to display the same message?
##

# Easier to toggle off log msgs after completing code and offers more control than print()

###
### What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
##

# Step OVER vs IN vs OUT of a 'child' function or statement loop

###
### After you click Continue, when will the debugger stop?
##

# Until end of program or next breakpoint

###
### What is a breakpoint?
##

# User set line of code to pause running program for debugging

