#1st way set automatically ignores duplicate element
s={10,20,30,20}
print("s =",s)

# 2nd method


s1=[10,20,30,20]
print("original list =",s1)
for x in s1:
    if (s1.count(x)>1):
        s1.remove(x)
print("new s1 =",s1)
