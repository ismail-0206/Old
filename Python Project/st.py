from lib2to3.pgen2.token import PLUS
from time import time

from tkinter import *
import os


def Restart():
    os.system("Restart -r -t 1")
    
def Restart_Time():
    os.system("Restart_Time -r -t 20")
    
def shutdown():
    os.system("shutdown -s -t 1")

sd=Tk()

sd.title("Shut Down App")
sd.geometry("567x567")
sd.config(bg="#006666")


rb=Button(sd,text="Restart",font=("arial",30,"bold"),bg="#0080FF",command=Restart)
rb.place(x=150,y=100,height=70,width=300)

rb=Button(sd,text="Restart Time",font=("arial",30,"bold"),bg="#0080FF",command=Restart_Time)
rb.place(x=150,y=200,height=70,width=300)

rb=Button(sd,text="Shut Down",font=("arial",30,"bold"),bg="#0080FF",command=shutdown)
rb.place(x=150,y=300,height=70,width=300)


sd.mainloop()
