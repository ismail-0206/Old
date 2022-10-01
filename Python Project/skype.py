from skpy import Skype

login=Skype("md02.06ismail2021@gmail.com","ismail567")

contect=login.contacts["live:.cid.966b4fd95fe6ce03"]
contect.chat.sendMsg("Hello!")


#for i in contect:
#    print(i)