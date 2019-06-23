import os
import sys
import time
import datetime
import random
from files import Blink
from Tkinter import Tk
win = Tk()
win.attributes("-alpha",1)
def Launcher(delay,start_time):
	time.sleep(delay)
	try:
		
		Blink#.Main().Screen()
	except:
		pass
	win.destroy()
	
	
if(__name__=="__main__"):
	Launcher(random.randrange(3,8),datetime.datetime.now())
	win.mainloop()