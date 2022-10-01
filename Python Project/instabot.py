from instabot import *
b=Bot()
b.login(username=(input("Enter Your User Name:\n")),password=(input("Enter your password:\n")))
b.follow(input("Please Enter your following username:\n"))