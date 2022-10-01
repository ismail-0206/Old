import smtplib as sl

ob=sl.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login("ismail567hacker@gmail.com","mylovepayel")
rec=input('Enter the receiver email address:\n')
massage="Subject:{}\n\n{}".format("Test","Hi! I'm ismail.")
ob.sendmail("ismail567hacker@gmail.com",rec,massage)
print("Thank You!")
ob.quit()