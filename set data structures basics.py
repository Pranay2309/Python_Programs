s={10,20,30,40,20}   #it does not allowes duplication of elements
print(type(s),s)

#add element in set
s1={10,20,30}
s1.add(40)
print(s1)

#update set
s2={10,20,30,60}
l=[40,50,10,70]
s2.update(l)
print("s2 =",s2)

#discard
s3={10,20,30,60}
print("old s3 =",s3)
s3.discard(60)
print(" new s3 =",s3)

#mathematical operation in sets

s4={30,70,80}
s5={10,20,30,60}
print("union set =",s4|s5)              #union 
print("difference set =",s5-s4)         #difference


