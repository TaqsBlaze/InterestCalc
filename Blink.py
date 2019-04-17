from Tkinter import *
import sqlite3,thread,os,time,random
import sys

"""
A simple Interest rate calculator
With monthly and yearly compound calculations
"""
#set program version and information

#//Declaring constant variables

Header_Title = "Blink";
_ProgramSize_ = '950x610+246+75';
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
window.geometry(_ProgramSize_);
window.title(_ProgramTitle_);
window.maxsize(950,610);
window.config(bg=Main_window_color);
window.iconbitmap(r'files/icon/logo.ico')

#PATCHS
try:
	from files.patchs import patch01
	from files.patchs import config_patch
	patch01.patch().menu(window)
except:
	pass








#//Lets get to the good stuff now!!
result_container=Frame()
result_container.configure(width=920,height=170,relief=RIDGE,border=4,bg='white')
result_container.place(x=15,y=430)
grid = Frame()
grid.configure(width=350,height=350,border=2,relief=RIDGE,bg='white',cursor='plus')
grid.place(x=15,y=70)
#//screen object (wasnt really necesary but why not)
screen = Frame()
screen.config(width=310,height=120,border=5,bg='black',cursor='circle')
screen.place(x=31,y=450)
global days;
global total_mark;
total_mark = 0.00
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
        More()._more_(P.get(),R.get(),T.get(),_InitCount_,total_mark)
        Label(window,text="Interest Rate Calculator",bg='green2',font='Angency 20 bold',fg='white',relief=RIDGE,border=2).pack(fill=BOTH);
        Label(grid,text='Principal($)',bg=Label_color,fg='black',font=Label_Font).place(x=_Const_,y=65);
        P.place(x=15,y=95);
        P.focus();
        Label(grid,text='Rate(%)',bg=Label_color,fg='black',font=Label_Font).place(x=_Const_,y=145);
        R.place(x=_Const_,y=170);

        def transition_thread(threadName,delay):
           
            #This function tries to bring a bit of transition effect on program_start_up
            #// works as expected but may need some proper way of doing it
            global visible
            visible = 0.0
            #window.attributes('-transparentcolor','green2') #This will make spacified color transparent in the window
            while(visible < 1.1):
                visible = visible +0.1
                time.sleep(0.1)
                window.attributes('-alpha',visible)

        Label(grid,text="Period[                               ]",bg=Label_color,fg='black',font=Label_Font).place(x=_Const_,y=225);
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
        years = Checkbutton(grid,text="Years",bg='white',font='roboto 9',variable = _Var2_,);
        years.configure(border=0);
        years.place(x=135,y=225);
        months.place(x=70,y=225);
        thread.start_new_thread(transition_thread,('transition',1))
    def Calculate(self):
       
        try:
            I = (float(P.get())*float(R.get())*float(T.get()))/100;
            print '%.2f'%I;
            _InitCount_ = I;
            y='%.2f'%I
            print type(y)
            u=float(y)
            #I_reslt=Label(window,text='Interest: {} {}'.format('$',_InitCount_),bg='lightgrey',fg='black',font='Consol 20 bold',width=17,height=3,border=3);
            # I_reslt.place(x=38,y=358);
            Container.configure(text='{} {}'.format('Interest: $','%.2f'%_InitCount_))
            total_mark = float(P.get()) + _InitCount_
            Total = Label(Container,text='Total: $ %.2f'%(total_mark),bg='lightgray',font=12)
            Total.place(x=45,y=68)
            screen.update();
            More()._more_(P.get(),R.get(),T.get(),_InitCount_,total_mark)
        except:
            pass
    
    def notice(self):
        win = Tk();
        win.geometry('410x500+250+150');
        win.maxsize(450,195);
        win.minsize(450,195);
        win.config(bg='white');
        win.title("NOTICE!")
        win_font = 'Calibri 12 bold';

        note ='''
        NOTICE
        Sorry this feature is still under development.
        The developer is working on bringing this feature on the
        next version release
        in the meantime please use the Years checkbox
        '''
        Label(win,text=note,font=win_font,bg='white',).pack();
        
        Button(win,text='Ok',width=15,font='britanic 13',command=win.destroy).pack() #close the notice window
        _Var_.set(0);   #Reseting the month checkbox to value 0
class Months(object):

    def calcMonths(self):
            I=(float(P.get())*float(R.get()))*(float(T.get())/12);
            Interest = float(I/100);
           
            Container.configure(text="Interest: $ %.2f"%final_state);
            total = float(P.get()) + final_state;
            Total = Label(Container,text='Total: $ %.2f'%total_mark,bg='lightgray',font='FB 12 underline');

            Total.place(x=45,y=68);
            More()._more_(P.get(),R.get(),T.get(),Interest,total);

class check():
    def checkformat(self):
        if(_Var_.get() == 1):
            Months().calcMonths();
        else:
            Main().Calculate();

class More():
#Getting things done in this framework was kind of tidius and crazy
#Had to find some go arounds and hacks to give somewhat readable data
#But will make a patch to clean up the mess soon!!!!!!

#data could only be passeed to this framwork globals do not work here
    def _more_(self,p,r,t,Interest,total):
        pass;
        period= _Var_.get();
        state='';
        if(period == 1):
            state = 'Months';
        elif(period != 1):
            state = 'Years';
        else:
            state = '';
       
	#-Converted these values in order to add the thousand separator (,)-#
        Interest = '%.2f'%(Interest);
	Interest = float(Interest);
        Total = '%.2f'%(total);
        Total = float(total);
	#--------------------------------------------------------------#
        More_info = Frame();
        More_info.configure(bg='white',width=530,height=345,border=1,relief=GROOVE,);
        More_info.place(x=402,y=70)
	Total = float(Total)
        try:

            data1=Label(More_info,font='Arial 15 bold',bg='white',fg='black',text='Invested amount: $ {:,}'.format(float(P.get())))
            data2=Label(More_info,font='Arial 15 bold',bg='white',fg='black',text='Percentage rate: {}%'.format(R.get()))
            data3=Label(More_info,font='Arial 15 bold',bg='white',fg='black',text='Time Invested: {} {}'.format(T.get(),state))
            data4=Label(More_info,font='Arial 15 bold',bg='white',fg='black',text='Interest: $ {:,}'.format(Interest))
            data5=Label(More_info,font='Arial 25 bold',bg='white',fg='black',text='Total Earnings: $ {:,}'.format(Tota))
      
            data1.place(x=2,y=5)
            data2.place(x=2,y=75)
            data3.place(x=2,y=140)
            data4.place(x=2,y=200)
            data5.place(x=2,y=290)
        except Exception,e:
			print e
			pass
			Label(More_info,text='BLINK',font='"Roman" 89 bold underline',bg='white',fg='black').place(x=66,y=120)
        print 'final:',final_state
        print 'Total:',total_mark
        #Info_container.configure(width=110,height=220)
        #Info_container.place(x=2,y=5)


if(__name__ == '__main__'):
    Main().Screen();
    window.mainloop();
