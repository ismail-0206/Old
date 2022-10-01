import re

email=("^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$")
user_email=input("Enter your Email:\n")

if re.search(email,user_email):
    print("Right Email")
else:
    print("Wrong Email")