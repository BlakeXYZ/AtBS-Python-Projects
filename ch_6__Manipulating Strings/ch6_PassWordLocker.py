                                                                                                        ###########
                                                                                                        ########
                                                                                                        # CH. 6 Password Locker Project
                                                                                                        ########
                                                                                                        ###########


import pyperclip

#! python3
# PassWordLocker.py - An insecure Password Locker

pwDict = {'Email': 'abc123',
          'Blog': 'chikachikaboom',
          'Myspace': 'BeepBoopXYZ'}

                                            # In Cmd Line, Enter argv. Make 'Account' Parameter equal that variable. (Input pwDict 'Key')
                                            #
pyperclip.copy(pwDict['Blog'])               # Copy Value from Key(argv) that is input

print("\n" + "Completed PassWordLocker.py Script" + "\n")

### ctrl+v = BeepBoopXYZ