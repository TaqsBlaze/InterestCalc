'''
Now the more splash screen
has been separated from the main program
/Cleaning Up/

by Tanaka Chinengundu
'''

def _more_(var,p,r,t,interest,total):
        from Tkinter import(
            Frame,
            Label,
            GROOVE
        )
        period= var
        state=''
        if(period == 1):
            state = 'Months'
        elif(period != 1):
            state = 'Years'
        else:
            state = '';
        #Had to convert these values in order to use the thousand separator#
        Interest = (interest);
        Interest = float(interest);
        Total = float(total);
        Total = float(Total);
        #-----------------------------------------------------------------#

        More_info = Frame();
        More_info.configure(bg='white',width=530,height=345,border=1,relief=GROOVE,);
        More_info.place(x=402,y=70);
        try:

            data1=Label(More_info,font='Arial 15 bold',bg='white',fg='black',text='Invested amount: $ {:,.2f}'.format(float(p)))
            data2=Label(More_info,font='Arial 15 bold',bg='white',fg='black',text='Percentage rate: {}%'.format(r))
            data3=Label(More_info,font='Arial 15 bold',bg='white',fg='black',text='Time Invested: {} {}'.format(t,state))
            data4=Label(More_info,font='Arial 15 bold',bg='white',fg='black',text='Interest: $ {:,.2f}'.format(Interest))
            data5=Label(More_info,font='Arial 25 bold',bg='white',fg='black',text='Total Earnings: $ {:,.2f}'.format(Total))
      
            data1.place(x=2,y=5)
            data2.place(x=2,y=75)
            data3.place(x=2,y=140)
            data4.place(x=2,y=200)
            data5.place(x=2,y=290)
        except Exception,e:
			#print 'Error in SPlashScreen:',e
			pass
			Label(More_info,text='BLINK',font='"Roman" 89 bold underline',bg='white',fg='black').place(x=66,y=120)
