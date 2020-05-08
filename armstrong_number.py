num=int(input("enter any three digit number\n"))
orgnum=num
n1=num%10
num=num//10
n2=num%10
num=num//10
rev=(n1*n1*n1)+(n2*n2*n2)+(num*num*num)
if rev==orgnum:
    print("entered number is a armstrong\n")
else:
    print("entered number is not a armstrong\n")
