import Tkinter,tkMessageBox



def ChangeLog():
	
	About=open(r'fileS/changelog.txt','r')
	About = About.read().strip('\n\s')
	label = tkMessageBox.showinfo("Change Log",About,)