from tkinter import *
import datetime


def time():
    time1 = datetime.datetime.now()
    
    hour=time1.strftime("%I")
    min=time1.strftime("%M")
    sec=time1.strftime("%S")
    am=time1.strftime("%p")
    
    
    date=time1.strftime("%d")
    date1=time1.strftime("%m")
    date2=time1.strftime("%y")
    date3=time1.strftime("%a")
    
    
    hlab.config(text=hour)
    hlab1.config(text=min)
    hlab2.config(text=sec)
    hlab3.config(text=am)
    hlab.after(200,time)
    
    hlab5.config(text=date)
    hlab6.config(text=date1)
    hlab7.config(text=date2)
    hlab8.config(text=date3)



dc=Tk()


dc.title("Digital Clock")
dc.geometry("800x500")
dc.config(background='#567567')

hlab=Label(dc,text="00",font=("Time new roman",50,"bold"),bg='#567765',fg='#a5c6d7')
hlab.place(x=50,y=50,height=100,width=100)

hlab1=Label(dc,text="00",font=("Time new roman",50,"bold"),bg='#567765',fg='#a5c6d7')
hlab1.place(x=220,y=50,height=100,width=100)

hlab2=Label(dc,text="00",font=("Time new roman",50,"bold"),bg='#567765',fg='#a5c6d7')
hlab2.place(x=430,y=50,height=100,width=100)

hlab3=Label(dc,text="00",font=("Time new roman",30,"bold"),bg='#567765',fg='#a5c6d7')
hlab3.place(x=640,y=50,height=100,width=100)



hlab5=Label(dc,text="00",font=("Time new roman",50,"bold"),bg='#567765',fg='#a5c6d7')
hlab5.place(x=50,y=220,height=100,width=100)

hlab6=Label(dc,text="00",font=("Time new roman",50,"bold"),bg='#567765',fg='#a5c6d7')
hlab6.place(x=220,y=220,height=100,width=100)

hlab7=Label(dc,text="00",font=("Time new roman",50,"bold"),bg='#567765',fg='#a5c6d7')
hlab7.place(x=430,y=220,height=100,width=100)

hlab8=Label(dc,text="00",font=("Time new roman",30,"bold"),bg='#567765',fg='#a5c6d7')
hlab8.place(x=640,y=220,height=100,width=100)

time()


dc.mainloop()