#def mygen():
    #yield 'A'
    #yield 'B'
    #yield 'C'
#g=mygen()
#print(type(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))


#EXAMPLE 2:

def countdown(num):
    print("Start Countdown")
    while(num>0):
        yield num
        num=num-1
values=countdown(5)
for x in values:
    print(x)
