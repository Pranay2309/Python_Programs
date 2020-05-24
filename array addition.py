from array import *
ar=array('i',[])
print("enter array elements")
for x in range(0,5):
    s=int(input(":"))
    ar.append(s)
sum=0
for y in range(0,5):
    sum=sum+ar[y]
print("sum=",sum)
