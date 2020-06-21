class one:
    a=100

class two(one):
    b=20
    def dis(self):
        print("a =",one.a,"b =",self.b)

ob1=two()
ob1.dis()
