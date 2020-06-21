a=12
b=0
try:
    print("before ")

    b=a/2
except ZeroDivisionError:
    print("exception executed")
#finally:                           #to execute in both the cases
    #print("finally block is executed")

print("after")
print("result",b)
