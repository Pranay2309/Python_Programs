num=int(input("enter any three digit number\n"))
orgnum=num
n1=num%10
num=num//10
n2=num%10
num=num//10
rev=(n1*100)+(n2*10)+(num*1)
if rev==orgnum:
    print("entered number is palindrome\n")
else:
    print("entered number is not a palindrome\n")
