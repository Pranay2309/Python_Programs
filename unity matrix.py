x=[[7,12,17],
   [18,45,19],
   [65,14,13]]
y=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[i])):
        y[i][j]=x[i][j]//x[i][j]
for r in y:
    print(r)
