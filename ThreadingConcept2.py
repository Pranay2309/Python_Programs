from threading import *
def display():
    for i in range(1,11):
        if i%2==0:
            print(i,end='  ')
        print()
t=Thread(target=display)      #creating thread object
t.start()
def display1():
    for i in range(1,11):
        if i%2!=0:
            print(i,end='  ')
        print()
t1=Thread(target=display1)      #creating thread object
t1.start()

