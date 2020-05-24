def add():
    """ Addition Program """
    print(add.__doc__)
    num1=int(input("Enter first number :"))
    num2=int(input("Enter second number :"))
    res=num1+num2
    print("Addition =",res)
def sub():
    """ Subtraction Program """
    print(sub.__doc__)
    num1=int(input("Enter first number :"))
    num2=int(input("Enter second number :"))
    res=num1-num2
    print("Subtraction =",res)
def multiplication():
    """ Multiplication Program """
    print(multiplication.__doc__)
    num1=int(input("Enter first number :"))
    num2=int(input("Enter second number :"))
    res=num1*num2
    print("Multiplication =",res)
def division():
    """ Division Program """
    print(division.__doc__)
    num1=int(input("Enter first number :"))
    num2=int(input("Enter second number :"))
    res=num1//num2
    print("Division =",res)
print("press 1 for addition\n")
print("press 2 for subtraction\n")
print("press 3 for multiplication\n")
print("press 4 for division\n")
ch=int(input("enter your choice\n"))
if ch==1:
    add()
elif ch==2:
    sub()
elif ch==3:
    multiplication()
elif ch==4:
    division()
else:
    print("Invalid Choice ")
