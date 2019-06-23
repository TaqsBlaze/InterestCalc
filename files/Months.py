from Tkinter import Label
from files import SplashScreen
'''
p=princepal
r=rate
t=time
VAR= the value to display time/period if months or years was ticked
'''
def calcMonths(Container,var,p,r,t):
        Interest=(float(p)*float(r))*(float(t)/12);
        Interest = float(Interest/100);
        Container.configure(text="Interest: $ {:,.2f}".format(Interest));
        total= float(p) + Interest;
        Total = Label(Container,text='Total: $ {:,.2f}'.format(total),bg='lightgray',font='FB 12');
        Total.place(x=45,y=68);
        VAR = var;
        SplashScreen._more_(VAR,p,r,t,Interest,total);