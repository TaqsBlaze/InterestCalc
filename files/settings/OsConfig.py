import os
#THIS FILE MAKES THE PROGRAM COMPATIBLE WITH WINDOWS OS 
#UNTIL BUGS ON LINUX OS ARE FIXD
#YOU COULD REMOVE ONLY FOR DEVELOPMENT PURPOSES

def Os(Os_0x,Window):

    if(Os_0x != 'nt'):
        Window.distroy();
    else:
        pass;