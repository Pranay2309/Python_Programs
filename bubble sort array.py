from array import *
ar=array('i',[])
for i in range(0,5):
    s=int(input("enter array elements: "))
    ar.append(s)
for i in range(0,5):
    for j in range(0,4):
        if(ar[j]>ar[j+1]):
            temp=ar[j]
            ar[j]=ar[j+1]
            ar[j+1]=temp
print("sorted array elements are:",ar)
