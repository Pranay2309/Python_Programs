a=12
b=0
add=0
try:
    x=int(input("enter number 1 :"))
    y=int(input("enter number 2 :"))
    add=x+y
    b=a/0
except Exception as msg:
    print("exception generated")
