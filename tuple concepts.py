t1=10,20,30   #type=tuple
t2=(10,20,30) #type=tuple


#conversion of list into tuple 

a=[10,20,30,2,12]
print(type(a))
t=tuple(a)
print(t,type(t),"length of tuple =",len(t))
print(t[0])

#slice operator in tuple
print(t[1:3])
print(t[::-1])   #reversing with the help of slice operator

#sorting the tuple
b=sorted(a)
print("sorted tuple : ",b)
print("min of tuple =",min(a),"\n","max of tuple =",max(a))
