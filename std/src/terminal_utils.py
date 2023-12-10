import os

def clear_terminal():
    # BRON: https://stackoverflow.com/questions/19596750/is-there-a-way-to-clear-your-printed-text-in-python
    # os.system executes a command
    # cls clears the system on windows
    # \033c is a ANSI escape code(https://en.wikipedia.org/wiki/ANSI_escape_code)
    #  signaling to the terminal that it needs to reset it self.

    # and then finally a if statement to check if the os is windows 
    # if it is not windows then printf the ANSI code
    # printf is "printf - format and print data" according to it's man page
    # printf is also a function in the c and c++(maybe) std

    os.system('cls' if os.name == 'nt' else "printf '\033c'")