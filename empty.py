f=open("empty.txt","a")
f.write("hello world")
f.close()
f=open("empty.txt","r")
#print(f.read())
for x in f:
    print(x)
f.close()

#create file when file is not created

f=open("NewFileCreatedByFileHandling.txt","x")
