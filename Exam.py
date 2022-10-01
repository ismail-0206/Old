c=int(input("Enter the number for List: "))
l=[]
m=[]
for i in range(0,c):
    b=(input("Enter the Name: "))
    a=int(input("Enter the Number: "))
    if a>=80:
        print(b,a,"Grade A+")
    elif a>=70:
        print(b,a,"Grade A")
    elif a>=60:
        print(b,a,"Grade B")
    elif a>=50:
        print(b,a,"Grade C")
    elif a>=40:
        print(b,a,"Grade D")
    else:
        print(b,a,"Grade F")
    l.append(b)
    m.append(a)
print(l)
print(m)
