from threading import *
def display():
    for i in range(1,11):
        print("Child Thread")
t=Thread(target=display)      #creating thread object
t.start()
for i in range(1,11):
   print("  Main Thread")
