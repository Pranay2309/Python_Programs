from threading import *
l=Lock()
l.acquire() 
l.release()
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(2):
        print("good evening:",end='')
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=("dhoni",))
t2=Thread(target=wish,args=("yuvraj",))
t3=Thread(target=wish,args=("kohli",))
t1.start()
t2.start()
t3.start()
