class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):     #
        return self.pages+other.pages

b1=book(100)
b2=book(200)
print(b1+b2)
print("total number of pages:",b1+b2)
