str1=input("enter any string\n")
if len(str1)<2:
    print(" ")
elif len(str1)>2:
    str2=str1[0:2]+str1[-2:]
    print(str2)
elif len(str1)==2:
    print(str1*2)
