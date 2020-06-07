def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter any number to find factorial :"))
if num<0:
    print("Factorial does not exists")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial =",fact(num))
    
