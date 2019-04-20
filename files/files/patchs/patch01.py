#//A PATCH FOR ADDING IN THE MENU SYSTEM TO THE ORIGINAL PROGRAM
#developed by Tanaka Chinengundu
from Tkinter import *
import os
import sys
#os.chdir("../")

class patch():
	
	def menu(self,window):
		menu = Menu(window,bg="green")
		window.config(menu=menu)
		settings = Menu(menu)
		menu.add_cascade(label="Settings",menu=settings)
		settings.add_command(label="themes",command=None)
		settings.add_command(label="methods",command=None)
		