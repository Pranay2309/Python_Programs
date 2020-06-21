class one:
    def __init__(self,x):
        print("class one constructor",x)
 

class two(one):
    b=20
    def __init__(self):
        super().__init__(self.b)
        print("two class constructor")

ob1=two()
