from ast import Pass
from distutils.log import error
from time import *
import random as r


def mistake(pc,user):
    error=0
    for i in range(len(pc)):
        try:
            if pc[i] != user[i]:
                error+=1
        except:
            error+=1
    return error

def st(sp1,sp2,spuser):
    td=time2-time1
    tr=round(td,2)
    st0=len(spuser)/tr
    return round(st0)

type=["""Musk was born to White South African parents in Pretoria, 
where he grew up.""","""He briefly attended the University of Pretoria 
before moving to Canada at age 17, acquiring citizenship through his 
Canadian-born mother.""","""He matriculated at Queen's University and transferred 
to the University of Pennsylvania two years later""","""where he received a bachelor's 
degree in Economics and Physics.""","""The company was bought by eBay in 
2002 for $1.5 billion."""]

t1=r.choice(type)
print(t1,"\n\n")

time1=time()
int1=input(":")
time2=time()

print("Speed: ",st(time1,time2,int1),"word/sec")
print("Error: ",mistake(type,t1))