from array import *
ar=array('i',[])
print("enter array elements\n")
for x in range(0,5):
    s=int(input(""))
    ar.append(s)
even=0
odd=0
for y in range(0,5):
    if ar[y]%2==0:
        even=even+ar[y]
    else:
        odd=odd+ar[y]
print("evensum=",even)
print("oddsum=",odd)
