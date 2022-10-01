import datetime
import time

et=datetime.datetime(2021,6,1)
site=["www.random.org"]
host="C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"

while True:
    if datetime.datetime.now()<et:
        print("start Blocking")
        with open(host,"r") as host_file:
            con=host.read()
            for website in site:
                if website not in con:
                    host_file.write(redirect+" "+website+"\n")
                else:
                    pass
    
    
    else:
        with open(host,'r') as host_file:
            con=host.readlines() 
            host_file.seek(0)
            for lines in con:
                if not any(website in lines for website in site):
                    host_file.write(lines)
            
            host_file.truncate()
        time.sleep(10)