class duck:
    def talk(self):
        print("quack...quack")
class dog:
    def talk(self):
        print("bow...bow")
class cat:
    def talk(self):
        print("meow...meow")
class goat:
    def talk(self):
        print("myaah...myaah")

def f1(obj):
    obj.talk()
l=[duck(),cat(),dog(),goat()]
for obj in l:
    f1(obj)
#x=duck()
#f1(x)
