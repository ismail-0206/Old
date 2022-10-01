from turtle import width
from sqlalchemy import true
from win32api import GetSystemMetrics
import numpy as np
import time
import cv2
import pyautogui

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
dim=(width,height)
f=cv2.VideoWriter_fourcc(*'XVID')
ot=cv2.VideoWriter('test.mp4',f,30.0,dim)
nt=time.time()
du=14
et=nt+du
while True:
    img=pyautogui.screenshot()
    f1=np.array(img)
    f2=cv2.cvtColor(f1,cv2.COLOR_BGR2RGB)
    ot.write(f2)
    t1=time.time()
    if t1>et:
        break
ot.release()
print("The End")