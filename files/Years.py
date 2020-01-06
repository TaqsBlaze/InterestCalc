import SplashScreen
from Tkinter import Label
def Calculate(Container,var,p,r,t,screen,tab1):
       
        try:
            Interest = (float(p)*float(r)*float(t))/100;
            _InitCount_ = Interest;
            Container.configure(text='{} {}'.format('Interest: $','{:,.2f}'.format(_InitCount_)))
            total= float(p) + _InitCount_
            Total = Label(Container,text='Total: $ {:,.2f}'.format(total),bg='lightgray',font=12)
            Total.place(x=45,y=68)
            screen.update();
            VAR = var
            SplashScreen._more_(VAR,p,r,t,_InitCount_,total,tab1)
        except Exception,e:
            print 'Error in Years:',e;
            pass