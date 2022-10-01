name=input("What's your Name?\n")

print("Welcome Mr",name.upper(),"It's a Adventure Game.\n"
      "Mr",name.upper(),"Please tell us, What you want Now?")

user=input("a normal man,an army or a terrorist?\n").lower()

score=1,"k"

if user=="normal man":
    print("WOW! You're a gteat person:)\n")
    print("Now what you want?\n")
    print("Mr",name,"?","Now you're in a poor life!\nDo you want to a Rich people?\n")
    user1=input("Choose One! a new bussiness or a Casino Game(with 10k Tk)\n").lower()
    
    if user1=="new bussiness" or user1=="bussiness":
        print("Oh no! You're lost it!")
    elif user1=="casino" or user1=="casino game":
        print("WOW! You got 10k Tk")
    else:
        print("LOL!")
        
elif user=="army":
    print("Oh! It's a life risk for you!\n")
    print("Mr",name.upper(),"if you want to change it, Now you can.\n")
    user2=input("normal man or terrorist.\nOtherwise write no\n").lower()
    
    if user2=="no":
        pass
    if user2=="new bussiness" or user2=="bussiness":
        print("Oh no! You're lost it!")
    elif user2=="casino" or user2=="casino game":
        print("WOW! You got 10k Tk\nYou Won it")
    else:
        print("LOL!")
    
           
elif user=="terrorist":
    pass



else:
    print("Invalid Input! You lost.")