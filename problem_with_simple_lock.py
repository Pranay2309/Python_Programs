from threading import *
l=Lock()
print("Main Thread trying to acquire Lock")
l.acquire()
print("Main Thread trying to acquire lock Again")
l.acquire()
