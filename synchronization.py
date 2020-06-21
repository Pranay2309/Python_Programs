from threading import *
import time
def wish(name):
    for i in range(5):
        print("good evening:",end='')
        time.sleep(2)
        print(name)
t1=Thread(target=wish,args=("dhoni",))
t2=Thread(target=wish,args=("yuvraj",))
t1.start()
t2.start()
