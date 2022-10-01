from cProfile import label
import time
from tkinter import *

r=Tk()
r.title("Digital Clock")
r.geometry("500x400")
r.config(bg="Black")

def s():
    text=time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(200,s)
label=Label(r,font=("Arial",50,"bold"),bg="Black",fg="Red",bd=140)
label.grid()


s()
r.mainloop()