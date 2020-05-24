x=[[1,1,1],
   [1,1,1],
   [1,1,1]]
y=[[1,1,1],
   [1,1,1],
   [1,1,1]]
sum=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[i])):
        sum[i][j]=x[i][j]+y[i][j]
for r in sum:
    print(r)
