# without extending thread class
from threading import *
class Test:
    def display(self):
        for i in range(1,11,2):
            print(i)
obj=Test()
t=Thread(target=obj.display)
t.start()
class Test1:
    def display(self):
        for i in range(2,11,2):
            print(i)
obj=Test1()
t=Thread(target=obj.display)
t.start()

