class one:
    a=10
    def __init__(self):
        self.b=30

    @staticmethod
    def m3():
        one.e=60

ob1=one()
one.m3()
print(one.__dict__)
