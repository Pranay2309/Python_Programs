from threading import *
import time
def display():
    print(current_thread().getName(),"...Started")
    time.sleep(3)
    print(current_thread().getName(),"...ended")
t1=Thread(target=display,name="ChildThread1")
t2=Thread(target=display,name="ChildThread2")
t1.start()
t2.start()
print(t1.name,"\nis Alive :",t1.is_alive())
print(t2.name,"is Alive :",t2.is_alive())
time.sleep(5)
print(t1,name,"is Alive :",t1.is_alive())
print(t1,name,"is Alive :",t1.is_alive())
