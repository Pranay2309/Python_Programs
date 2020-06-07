a=12              #global variable
def fun1():
    a=2          #local variable
    print(a)
    print(globals()['a'])

    
fun1()

