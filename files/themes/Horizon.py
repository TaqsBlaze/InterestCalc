#THEME PACK DEVELOPED BY TANAKA CHINENGUNDU

#:HORIZON/


def Horizon(WindowColor,Label1,Label2,P,R,T,Container,Screen,Months,Years):
	Border=3
	Colors='''gray orange white'''.split()
	Main = WindowColor;
	Label = Label1;
	Label2 = Label2;
	Screen = Screen;
	Month = Months;
	Year = Years;
	Main.configure(bg=Colors[0]);
	Label.configure(bg=Colors[0]);
	Label2.configure(bg=Colors[0]);
	#Entry.configure(bg=Colors[0][0]);
	Screen.configure(bg=Colors[0]);
	P.configure(bg=Colors[0],border=Border);
	R.configure(bg=Colors[0],border=Border);
	T.configure(bg=Colors[0],border=Border);
	Month.configure(bg=Colors[0]);
	Year.configure(bg=Colors[0]);
	Screen.configure(bg=Colors[1]);
	Container.configure(bg=Colors[0],border=Border);

