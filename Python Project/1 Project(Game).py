print("Welcome to our world")

score=0

while True:
    
        qus1=input("CPU?\n")

        if qus1.lower()=="central processing unit":
            print("Correct:)\n")
            score+=1
        else:
            print("Incorrect!\n")
            score-=0.5

        qus2=input("GPU?\n")

        if qus2.lower()=="graphics processing unit":
            print("Correct:)\n")
            score+=1
        else:
            print("Incorrect!\n")
            score-=0.5

        qus3=input("RAM?\n")

        if qus3.lower()=="random access memory":
            print("Correct:)\n")
            score+=1
        else:
            print("Incorrect!\n")
            score-=0.5

        qus4=input("PS?\n")

        if qus4.lower()=="power supply":
            print("Correct:)\n")
            score+=1
        else:
            print("Incorrect!\n")
            score-=0.5

        qus5=input("PC?\n")

        if qus5.lower()=="personal computer":
            print("Correct:)\n")
            score+=1
        else:
            print("Incorrect!\n")
            score-=0.5

        qus6=input("Top Billioner?\n")

        if qus6.lower()=="elon mask":
            print("Correct:)\n")
            score+=1
        else:
            print("Incorrect!\n")
            score-=0.5

        print("You got" + str(score) + "Point\n")
        print("You got" + str((score/6)*100) + "%.\n")