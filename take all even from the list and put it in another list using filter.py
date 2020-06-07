def even(x):
    if x%2==0:
        return True
    else:
        return False
l=[1,5,10,20]
print("List =",l)
newlist=tuple(filter(even,l))
print("Tuple =",newlist)
