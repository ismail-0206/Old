from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

ob=Tk()


ob.title("Translator")
ob.geometry("500x650")
ob.configure(background="#567567")

labtext=Label(ob,text="Translator",font=("Latin",50,"bold"),bg="#567567",fg="white")
labtext.place(x=80,y=50,width=340,height=50)

labtext=Label(ob,text="Source Text",font=("Latin",20,"bold"),bg="#567567",fg="#abcdef")
labtext.place(x=100,y=150,width=300,height=50)

labtext=Label(ob,text="To",font=("Latin",20,"bold"),bg="#567567",fg="#abcdef")
labtext.place(x=100,y=210,width=80,height=30)

frame=Frame(ob).pack(side=BOTTOM)
source=Text(frame,font=("Arial",20,"bold"),wrap=WORD)
source.place(x=20,y=240,width=460,height=150)

frame=Frame(ob).pack(side=BOTTOM)
source=Text(frame,font=("Arial",20,"bold"),wrap=WORD)
source.place(x=20,y=400,width=460,height=150)

button=Button(frame,text="Translate",font=("Latin",20,"bold"),bg="#abcdef",fg="white",relief=RAISED)
button.place(x=240,y=210,width=235,height=30)

list=list(LANGUAGES.values())
comb=ttk.Combobox(frame,value=list,font=("Latin",8),state="readonly")
comb.place(x=20,y=210,width=90,height=30)
comb.set("English")

comb1=ttk.Combobox(frame,value=list,font=("Latin",8),state="readonly")
comb1.place(x=170,y=210,width=90,height=30)
comb1.set("English")


ob.mainloop()