list1=[]
x=int(input("enter number of elements\n"))
for i in range(1,x+1):
    array=int(input("enter array elements: "))
    list1.append(array)
print("largest element in the array is: ",max(list1))
