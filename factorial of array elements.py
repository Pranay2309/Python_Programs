from array import *
num=array('i',[])
for x in range(0,5):
    num.append(int(input("enter tha array elements to find factorial\n")))
fact=1
for a in range(0,5):
    for b in range(1,num[a]+1):
        fact=fact*b
    print("factorial of",num[a],"is",fact)
    fact=1
    
