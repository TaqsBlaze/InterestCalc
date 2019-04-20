#Main window dimansions
#icon
#color
#and title properties
def Main_Window(window,_ProgramSize_,_ProgramTitle_,Main_window_color):
    window.geometry(_ProgramSize_);
    window.title(_ProgramTitle_);
    window.config(bg=Main_window_color);
    window.iconbitmap(r'files/icon/logo.ico')
    window.maxsize(950,620);
    window.minsize(950,620);