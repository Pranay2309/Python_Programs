l=[1,2,3,4,5]
print("Old List =",l)
def double(x):
    return 2*x
new=list(map(double,l))
print("New =",new)

#map using lambda
a=[10,20,30]
print("a =",a)
new=tuple(map(lambda x:2*x,a))
print("New =",new)
