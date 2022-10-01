from email import message
from socket import timeout
import time
from plyer import notification

if __name__=='__main__':
    
        while True: 
            notification.notify(
                title="Take Rest",
                message="You're alredy pass your Time.",
                #app_icon="F:\Coding Project\logo.png",
                timeout=15)
            time.sleep(3600)