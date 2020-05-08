print("press + for addition\n")
print("press - for subtraction\n")
print("press * for multiplication\n")
print("press // for division\n")
ch=input("enter your choice\n")
if ch=='+':
    print("Addition program\n")
    num1=int(input("enter first number for addition\n"))
    num2=int(input("enter second number for addition\n"))
    res=num1+num2
    print("Addition=",res)
elif ch=='-':
    print("Subtraction program\n")
    num1=int(input("enter first number\n"))
    num2=int(input("enter second number\n"))
    res=num1-num2
    print("subtraction=",res)
elif ch=='*':
    print("Multiplication program\n")
    num1=int(input("enter first number\n"))
    num2=int(input("enter second number\n"))
    res=num1*num2
    print("multiplication=",res)
elif ch=='//':
    print("Division program\n")
    num1=int(input("enter first number\n"))
    num2=int(input("enter second number\n"))
    res=num1//num2
    print("Division=",res)
else:
    print("Invalid Option\n")
    
