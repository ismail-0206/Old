from tkinter import *
import speedtest


def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    ds=str(round(sp.download()/(10**6),3))+"Mbps"
    us=str(round(sp.upload()/(10**6),3))+"Mbps"
    lab1.config(text=ds)
    lab2.config(text=us)


sp=Tk()

sp.title("Inernet Speed Test")
sp.geometry("500x550")
sp.config(bg="Black")

lab=Label(sp,text=("Inernet Speed"),font=("The new Roman",40,"bold"),bg="Black",fg="Gray")
lab.place(x=80,y=40,height=50,width=360)

lab=Label(sp,text=("Downloading Speed"),font=("The new Roman",20,"bold"),bg="#F0F8FF",fg="Gray")
lab.place(x=80,y=150,height=50,width=360)

lab1=Label(sp,text=("00"),font=("The new Roman",20,"bold"),bg="#F0F8FF",fg="Gray")
lab1.place(x=80,y=220,height=50,width=360)

lab=Label(sp,text=("Uploading Speed"),font=("The new Roman",20,"bold"),bg="#F0F8FF",fg="Gray")
lab.place(x=80,y=290,height=50,width=360)

lab2=Label(sp,text=("00"),font=("The new Roman",20,"bold"),bg="#F0F8FF",fg="Gray")
lab2.place(x=80,y=360,height=50,width=360)

button=Button(sp,text="Speed Check",font=("The new Roman",20,"bold"),bg="gray",fg="Black",command=speedcheck)
button.place(x=80,y=430,height=50,width=360)

sp.mainloop()