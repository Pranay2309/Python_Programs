num=int(input("enter any number\n"))
sum=0
while(num>0):
    n1=num%10
    sum=sum+n1
    num=num//10
print("sum=",sum)
