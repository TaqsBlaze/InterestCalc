from Tkinter import *
import thread,os,time
import sys

#Part system imports/
from files import SplashScreen
from files import Years,Months
from files.files.UI import UI_transition
from files.files.UI import WindowProperties
from files.files.UI import Extras
"""
==========================================================================================================
                                A simple interest rate calculator
                                 Developed by Tanaka Chinengundu
==========================================================================================================
"""
#//Declaring constant variables

Header_Title = "Blink";
_ProgramSize_ = '950x700+246+75';
_ProgramVersion_= '1.5.10';
_ProgramTitle_ = "{} [version:{}]".format(Header_Title,_ProgramVersion_);
_Font_='Arial 15 bold italic';
Label_Font = 'Consolus 12'
Main_window_color = 'white';
Label_color = Main_window_color;
_EntryWidth_ = 18;
_EntryHieght_ = 13;
_Const_ = 15;
Entry_Border = 2;

#//Main window object
window = Tk();
WindowProperties.Main_Window(window,_ProgramSize_,_ProgramTitle_,Main_window_color);

#PATCHS
try:
	from files.patchs import patch01
	patch01.patch().menu(window);
except:
	pass








#//Lets get to the good stuff now!!
Extras.extras();
screen = Frame();
screen.config(width=310,height=120,border=5,bg='black',cursor='circle');
screen.place(x=31,y=450);
  
#//screen object (wasnt really necesary but why not)
grid = Frame();
grid.configure(width=350,height=350,border=2,relief=RIDGE,bg='white',cursor='plus');    grid.place(x=15,y=70);
global days;
global total_mark;
total_mark = 0.00;
#//Main process
class Main(object):
    global total_mark;
    global final_state;
    global _Principal_;
    global _Rate_;
    global _Time_;
    global _Interest_;
    global _InitCount_;
    global Container;
    global _Var_;
    global P;
    global R;
    global T;
    global total_mark;
    global visible
    visible = 0.0
    final_state = ''
    _Principal_ = IntVar();
    _Rate_ = IntVar();
    _Time_ = IntVar();
    _Var_ = IntVar();
    _InitCount_ = float(0)
    _Rate_.set('')
    _Time_.set('')
    _Principal_.set('')
    P = Entry(grid,relief=GROOVE,textvariable=_Principal_,font=_Font_,width=_EntryWidth_,border=Entry_Border);
    R = Entry(grid,relief=GROOVE,textvariable=_Rate_,font=_Font_,width=_EntryWidth_,border=Entry_Border,);
    T = Entry(grid,relief=GROOVE,textvariable=_Time_,font=_Font_,width=_EntryWidth_,border=Entry_Border);
    Container = Label(screen,text='Interest:$ %.2f'%_InitCount_,font='Consol 20 bold',bg='lightgray',fg='black',width=17,height=3,border=3);
    Container.configure(relief=RIDGE,border=3)
#//Now lets render our screen
    
    window.attributes('-topmost',0)
    sys._getframe(0).f_code.co_name
    def Screen(self):
        
        
        visibility=window.attributes('-alpha',visible)
        SplashScreen._more_(_Var_.get(),P.get(),R.get(),T.get(),_InitCount_,total_mark)
        Label(window,text="Interest Rate Calculator",bg='green2',font='Angency 20 bold',fg='white',relief=RIDGE,border=2).pack(fill=BOTH);
        Label(grid,text='Principal($)',bg=Label_color,fg='black',font=Label_Font).place(x=_Const_,y=65);
        P.place(x=15,y=95);
        P.focus();
        Label(grid,text='Rate(%)',bg=Label_color,fg='black',font=Label_Font).place(x=_Const_,y=145);
        R.place(x=_Const_,y=170);

        
        Label(grid,text="Period[\t\t        ]",bg=Label_color,fg='black',font=Label_Font).place(x=_Const_,y=225);
        T.place(x=_Const_,y=250);
        Button(grid,text='calculate',bg='red',fg='white',border=2,relief=RIDGE,font="Roboto 10 bold",width=15,command=check().checkformat).place(x=36,y=309);
        global months;
        global years;
        global d;
        global _Var_
        global _Var2_
        _Var_ = IntVar()
        _Var2_= IntVar()
        _Var_.set(0)
        d = Container.place(x=1,y=3);
        months = Checkbutton(grid,text="Months",bg='white',font='roboto 9',variable=_Var_,command=None);
        years = Checkbutton(grid,text="Years",bg='white',font='roboto 9',variable = _Var2_,command=None);
        years.configure(border=0);
        years.place(x=135,y=225);
        months.place(x=70,y=225);
        thread.start_new_thread(UI_transition.transition_thread,('transition',1,window))

class check():
    def checkformat(self):
        if(_Var_.get() == 1):
            Months.calcMonths(Container,_Var_.get(),P.get(),R.get(),T.get());
        else:
            Years.Calculate(Container,_Var_.get(),P.get(),R.get(),T.get(),screen);



if(__name__ == '__main__'):
    Main().Screen();
    window.mainloop();
