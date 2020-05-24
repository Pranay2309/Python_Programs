x=[[7,12,17],
   [18,45,19],
   [65,14,13]]
print("matrix after conversion in diagonal matrix : ")
for i in range(len(x)):
    for j in range(len(x[i])):
        if i!=j:
            x[i][j]=0
for r in x:
    print(r)
