num=int(input("Enter any number\n"))
orgnum=num
rev=0
while(num>0):
    n1=num%10
    rev=rev*10+n1
    num=num//10
print(rev)
if orgnum==rev:
    print("The number is palindrome\n")
else:
    print("The number is not a palindrome\n")
