#concatenation of tuple
t1=1,20,3,4,50
t2=5,4,3,2,1
print(t1+t2)

#slice operator
print(t1[::-1],len(t1))

#minimum and maximum
print(min(t1),max(t1))

b=sorted(t1)
print(b)

#adding of tuple elements

sum=0
for i in range(0,5):
    sum=sum+t1[i]
print(sum)

#sorting even and odd elements:
t=(1,52,56,49,3)
even=0
odd=0

for i in range(0,5):
    if(t[i]%2==0):
        print(t[i])

b=t.index(52)
print(b)

#comparison of two tuple

#t1=1,2,3,4,5
#t2=1,2,3,4,5
#x=t1.cmp(t2)


