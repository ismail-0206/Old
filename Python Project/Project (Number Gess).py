import random


a=input("Gess a number:)\n")


if a.isdigit:
    a=int(a)
        
    if a<=0:
        print("Please type a digit larger then 0.\n")
        quit()

else:
    print("Please type a digit\n")
    quit()
    
   
r=random.randrange(0,a)

s=0

while True:
    s+=1
    b=input("gess it:)")
    
    if b.isdigit():
        b=int(b)
          
    else:
        print("Oh no!\n")
        continue
    
    if b==r:
        print("Oh you're got it")
        break
    
    else:
        if b>r:
            print("you're upper then it!")
        else:
            print("you're lower then ot!")    
            
print("You got in: " + str(s))