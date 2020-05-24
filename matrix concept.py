n=[[1,2,3],[4,5,6],[7,8,9]]
print(n)
print("elements by row wise:")
for r in n:
    print(r)
print("print elements by matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()
