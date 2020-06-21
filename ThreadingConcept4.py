#using thread class
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(1,11,2):
            print(i)
t=MyThread()
t.start()
class MyThread1(Thread):
    def run(self):
        for i in range(2,11,2):
            print(i)
t=MyThread1()
t.start()
