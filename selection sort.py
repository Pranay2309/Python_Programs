from array import *
ar=array('i',[])
for i in range(0,5):
    ar.append(int(input("enter array elements")))
for i in range(0,5):
    for j in range(i+1,5):
        if ar[i]>ar[j]:
            temp=ar[i]
            ar[i]=ar[j]
            ar[j]=temp
print("sorted array elements are :",ar)
    
