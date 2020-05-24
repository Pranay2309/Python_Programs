dict={100:"data1",200:"data2",300:"data3"}
print(dict)
#pop item 
print(dict.popitem())

#key and value
for k,v in dict.items():
    print(k,"__",v)

#copy function
dict1=dict.copy()
print(dict1)

#get value

print(dict.get(100))

#keys
#print(dict.keys())
#for k in dict.keys():
    #print(k)

#set default
print(dict.setdefault(400,"data4"))
print(dict)

#update dictionary
x={500:"data5",600:"data6"}
dict.update(x)
print(dict)
