print("press 1 for addition\n")
print("press 2 for subtraction\n")
print("press 3 for multiplication\n")
print("press 4 for division\n")
ch=int(input("enter your choice\n"))
if ch==1:
    print("Addition program\n")
    num1=int(input("enter first number for addition\n"))
    num2=int(input("enter second number for addition\n"))
    res=num1+num2
    print("Addition=",res)
elif ch==2:
    print("Subtraction program\n")
    num1=int(input("enter first number\n"))
    num2=int(input("enter second number\n"))
    res=num1-num2
    print("subtraction=",res)
elif ch==3:
    print("Multiplication program\n")
    num1=int(input("enter first number\n"))
    num2=int(input("enter second number\n"))
    res=num1*num2
    print("multiplication=",res)
elif ch==4:
    print("Division program\n")
    num1=int(input("enter first number\n"))
    num2=int(input("enter second number\n"))
    res=num1//num2
    print("Division=",res)
else:
    print("Invalid Option\n")
    
