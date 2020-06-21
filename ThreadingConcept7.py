from threading import *
def dis():
    for i in range(1,10):
        print("Child thread :",current_thread().ident)
t=Thread(target=dis)
t.setName("pranay2309")
t.start()
t1=Thread(target=dis)
t1.setName("pranay2309")
t1.start()

for i in range(1,11):
    print("main thread :",current_thread())
