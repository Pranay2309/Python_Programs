num=int(input("Enter any number\n"))
orgnum=num
sum=0
for v in range(num,0,-1):
    n=num%10
    sum=sum+n**3
    num=num//10
if orgnum==sum:
    print("The number is a armstrong number\n")
else:
    print("The number is not a armstrong number\n")
