from os import name

def Os(Window):
    Os_x0= name
    if(Os_x0 != "nt"):
        Window.distroy()
    else:
        pass
