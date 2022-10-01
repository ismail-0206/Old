import random

user_score=0
pc_score=0
op=["rock","paper","Scisser"]


while True:
    user=input("Pick Rock, Paper,Scisser 'q' to Quit:\n").lower()
    print("You Won ",str(user_score),)
    print("PC won ",str(pc_score),"\n")
    if user == "q":
        print("Bye!\n")
        break
    if user not in op:
        continue
    
    ran_num=random.randint(0,2)
    
    pc_pick=op[ran_num]
    
    if user=="rock" and pc_pick=="paper":
        print("pc won!\n")
        pc_score+=1
        
    elif user=="scisser" and pc_pick=="rock":
        print("pc won!\n")
        pc_score+=1
        
    elif user=="paper" and pc_pick=="scisser":
        print("pc won!\n")
        pc_score+=1
    else:
        print("You Won:)\n")
        user_score+=1

print("You Won ",str(user_score),)
print("PC won ",str(pc_score),)
if user_score<pc_score:
    print("Oh no! You lost this game.")
elif user_score>pc_score:
    print("WOW! You're won it:)")
else:
    print("Oh! you & pc both same. Try again.")