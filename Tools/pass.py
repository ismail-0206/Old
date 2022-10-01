from random import *

user=input("Enter:\n")
password=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}",";",":","'","\"",",",".","<",">","/","?","|","\\","~","`"," "]

gess=""

while(gess!=user):
    gess=""
    
    for i in range(len(user)):
        gess+=password[randint(0,len(password)-1)]
        print(gess)

print("Password is:",gess)