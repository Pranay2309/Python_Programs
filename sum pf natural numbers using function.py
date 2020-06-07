def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)
num=int(input("Enter natural number"))
if num<0:
    print("Enter positive number")
else:
    print("Sum of natural number =",sum(num))
    
    
